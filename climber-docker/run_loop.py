from os import path, chdir
import argparse
import time
import ConfigParser
import subprocess
import grasshopper_controller
import climber_controller
# from icecream import ic

_cli_defaults_fname = 'cli_defaults.cfg'
_loop_params_fname = '_loop_params.cfg'


def parse_cli_args():
    pass

def _get_cli_args():
    mainparser = argparse.ArgumentParser(
        prog='proteins-loop',
        description=(
            "A tool that does clever stuff with modelling proteins."
        )
    )

    mainparser.add_argument(
        '--input-pdb',
        metavar='Input PDB file',
        help=('The Input PDB file.')
    )

    mainparser.add_argument(
        '--input-csv',
        metavar='Input CSV file',
        help=('The Input CSV file.')
    )

    mainparser.add_argument(
        '--experiment-id',
        metavar='Experiment ID',
        help=('The Experiment ID.')
    )


    mainparser.add_argument(
        '--check-cli-defaults',
        action='store_true',
        help=('Check the paths to the external components are valid. Specifically it checks:\n'
              ' * That the `cli_defaults.cfg` file exists and can be loaded.'
              ' * The path to the Rhino.exe is valid'
              ' * The path to the Grasshopper (`.gh`) file is valid'
              ''
              'NOTE: This does not check that Rhino is licensed.' )
    )

    mainparser.add_argument(
        '--create-cli-defaults',
        action='store_true',
        help=('Creates (or overwrites) the `cli_defaults.cfg` file with some reasonable defaults.' )
    )

    mainparser.add_argument(
        '--check-docker-image',
        action='store_true',
        help=('Checks that the Climber Docker image is available and up to date. Specifically it checks:\n'
              ' * That `docker` is in the system path'
              ' * The path to the docker-credentials-* tool is valid'
              ' * That the `docker` CLI tool is logged into Docker Hub with the relevant credentials.'
              ' * That the Climber Docker image has been downloaded from Docker Hub.' )
    )

    mainparser.add_argument(
        '--pull-docker-image',
        action='store_true',
        help=('Downloads the Climber Docker image specified in `cli_defaults.cfg` from Docker Hub.' )
    )

    return mainparser


def write_cli_defaults_file():
    """
    (Over)writes a `cli_defaults.cfg` file, with a reasonable set of hard coded defaults.
    """
    cli_defaults = ConfigParser.RawConfigParser()
    cli_defaults.add_section('rhino_grasshopper')
    cli_defaults.set('rhino_grasshopper', 'rhino_exe_fname', 'rhino.exe')
    cli_defaults.set('rhino_grasshopper', 'rhino_dir', 'C:/Program Files/Rhino 7/System')
    cli_defaults.set('rhino_grasshopper', 'grasshopper_file', "gh_loop_with_cli.gh")

    cli_defaults.add_section('climber')
    cli_defaults.set('climber', 'docker_credentials', "C:/Program Files/Docker/Docker/resources/bin/docker-credential-wincred.exe")
    cli_defaults.set('climber', 'docker_username', 'climberapp')
    cli_defaults.set('climber', 'docker_image_name', 'climberapp/climber-test')
    cli_defaults.set('climber', 'docker_image_ver', 'latest')

    cli_defaults.add_section('shared')
    cli_defaults.set('shared', 'shared_dir', 'RUN101')

    cli_defaults_fpath = get_cli_defaults_fpath()
    #    _config_fpath = path.join(rs.DocumentPath(), '_loop_params.cfg')

    with open(cli_defaults_fpath, 'wb') as cli_defaults_file:
        cli_defaults.write(cli_defaults_file)


def get_cli_defaults_fpath():
    return path.join(path.dirname(path.realpath(__file__)), _cli_defaults_fname)


def read_cli_defaults_file():
    cli_defaults = ConfigParser.RawConfigParser()

    _config_fpath = get_cli_defaults_fpath()

    try:
        with open(_config_fpath, 'rb') as cli_defaults_file:
            cli_defaults.readfp(cli_defaults_file)
    except IOError:
        raise ValueError('The configuation file could not be found at\n\t{0}'.format(_config_fpath))
    except ConfigParser.Error:
        raise ValueError('There was a problem with reading then contents of the file at\n\t{0}'.format(_config_fpath))

    return cli_defaults


def write_gh_args_file(input_pdb, input_csv, experiment_id):
    config = ConfigParser.RawConfigParser()
    config.add_section('InputFiles')
    config.set('InputFiles', 'input_pdb', input_pdb)
    config.set('InputFiles', 'input_csv', input_csv)
    config.set('InputFiles', 'experiment_id', experiment_id)
    config.add_section('OutputFiles')
    config.set('OutputFiles', 'outout_pdb', 'Five')

    _config_fpath = path.join(path.dirname(path.realpath(__file__)), _loop_params_fname)
    #    _config_fpath = path.join(rs.DocumentPath(), '_loop_params.cfg')

    with open(_config_fpath, 'wb') as configfile:
        config.write(configfile)


def read_gh_args_files():
    """
    Returns a tuple with paths to input_pdb, input_csv
    """
    config = ConfigParser.RawConfigParser()

    _config_fpath = path.join(path.dirname(path.realpath(__file__)), _loop_params_fname)
#    _config_fpath = path.join(rs.DocumentPath(), '_loop_params.cfg')

    with open(_config_fpath, 'rb') as param_file:
        config.readfp(param_file)
        print(config.sections())
        input_pdb = config.get('InputFiles', 'input_pdb')
        input_csv = config.get('InputFiles', 'input_csv')
        experiment_id = config.get('InputFiles', 'experiment_id')

    return (input_pdb, input_csv, experiment_id)


def get_host_shared_dir_path(cli_defaults):
    shared_dir_name = cli_defaults.get('shared', 'shared_dir')
    host_shared_dir_path = path.abspath(path.join(path.dirname(get_cli_defaults_fpath()), shared_dir_name))
    if path.exists(host_shared_dir_path) and path.isdir(host_shared_dir_path):
        return host_shared_dir_path

    raise ValueError('ERROR: Cannot locate shared directory. Directory does not exist:'
                     '\n{}'.format(host_shared_dir_path))

def check_file_param_is_valid(file_name, cli_defaults):
    """
    If `file_name` is relative then assume that it is relative to the shared dir and check it exists.
    If `file_name` is absolute then check it both exists and is inside the shared dir
    """
    host_shared_dir_path = get_host_shared_dir_path(cli_defaults)

    # Check
    if path.isabs(file_name):
        abs_fpath = file_name
    else:
        abs_fpath = path.abspath(path.join(host_shared_dir_path, file_name))

    common_root = path.abspath(path.commonprefix([host_shared_dir_path, abs_fpath]))
    if common_root != host_shared_dir_path:
        raise ValueError('ERROR: The file `{}` is not within the shared directory `{}`.'
                         ' Hence it cannot be made available to both GrassHopper and Climber.'.format(
                             file_name, host_shared_dir_path
                         ))


if __name__ == "__main__":

    mainparser = _get_cli_args()
    args = mainparser.parse_args()

    if args.create_cli_defaults:
        write_cli_defaults_file()
        exit(0)

    cli_defaults = read_cli_defaults_file()

    if args.check_cli_defaults:
        try:
            grasshopper_controller.check_grasshopper_globals(cli_defaults, _cli_defaults_fname)
            exit(0)
        except (ValueError, ConfigParser.Error) as ve:
            print(ve)
            exit(1)

    if args.check_docker_image:
        try:
            climber_controller.check_climber_globals(cli_defaults, _cli_defaults_fname)
            exit(0)
        except (ValueError, ConfigParser.Error) as ve:
            print(ve)
            exit(2)

    if args.pull_docker_image:
        try:
            climber_controller.pull_climber_docker_image(cli_defaults)
            exit(0)
        except (ValueError, ConfigParser.Error) as ve:
            print(ve)
            exit(3)

    # Assume that we actually want to do something useful here
    # Check that both `--input-pdb` and `--input-csv` have been specificed
    if args.input_pdb and args.input_csv and args.experiment_id:
        print('Yay! let do something useful here!')

        check_file_param_is_valid(args.input_pdb, cli_defaults)
        check_file_param_is_valid(args.input_csv, cli_defaults)

        write_gh_args_file(args.input_pdb, args.input_csv, args.experiment_id)
        container_id = climber_controller.launch_climber(cli_defaults)
        grasshopper_controller.launch_grasshopper(cli_defaults)
        climber_controller.stop_background_docker(container_id)
        exit(0)

    print('Oh - probably missing one or more required parameters.')
