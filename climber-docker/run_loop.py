from os import path
import time
from ConfigParser import RawConfigParser

# The abs path to the grasshopper file with the loop logic
grasshopper_file = "gh_loop_with_cli.gh"
grasshopper_fpath = path.join(path.dirname(path.realpath(__file__)), "gh_loop_with_cli.gh")

# The abs path to a dummy (blank) Rhino3D file, require as a commandline param, but of no other use.
rhino3d_dummy_file = ""



def parse_cli_args():
    pass


def write_gh_args_file():
    config = RawConfigParser()
    config.add_section('InputFiles')
    config.set('InputFiles', 'input_pdb', 'Three')
    config.set('InputFiles', 'input_csv', 'Four')
    config.add_section('OutputFiles')
    config.set('OutputFiles', 'outout_pdb', 'Five')


    _config_fpath = path.join(path.dirname(path.realpath(__file__)), '_loop_params.cfg')
    #    _config_fpath = path.join(rs.DocumentPath(), '_loop_params.cfg')

    with open(_config_fpath, 'wb') as configfile:
        config.write(configfile)


def read_gh_args_files():
    """
    Returns a tuple with paths to input_pdb, input_csv
    """
    config = RawConfigParser()
    print('config.options()')
    print(config.sections())
    print('done')


#    print(rs.DocumentPath())
    # print(dir(rs))

    _config_fpath = path.join(path.dirname(path.realpath(__file__)), '_loop_params.cfg')
#    _config_fpath = path.join(rs.DocumentPath(), '_loop_params.cfg')

    with open(_config_fpath, 'rb') as param_file:
        config.readfp(param_file)
        print(config.sections())
        input_pdb = config.get('InputFiles', 'input_pdb')
        input_csv = config.get('InputFiles', 'input_csv')


    return (input_pdb, input_csv)




def call_grasshopper():
    """
    cd **PATH TO DIRECTORY CONTAINING GH FILE**
    "**PATH TO RHINO.EXE**" /nosplash /runscript="-grasshopper editor load document open **GRASSHOPPER FILE NAME** _enter" "**PATH TO ASSOCIATED RHINO FILE**"
    """
    # cd C:\Users\jrams\Desktop
    # Generally assumed to be constant
    rhino_exe_path = "C:\Program Files\Rhinoceros 5 (64-bit)\System\rhino.exe"
    # What happens if `grasshopper_file` contains a space?
    rhino_args = '/nosplash /runscript="-grasshopper editor load document open {0} _enter" "{1}"'.format(grasshopper_fpath, rhino3d_dummy_file)



if __name__ == "__main__":
    input_pdb = ""
    input_csv = ""

    print('writing to cfg')
    write_gh_args_file()
    print('reading from cfg')
    time.sleep(0)
    read_gh_args_files()