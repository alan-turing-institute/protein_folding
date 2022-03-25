
from os import path, devnull, chdir
import subprocess
import re

def check_climber_globals(cli_defaults, cli_config_fname):
    """
    ' * That `docker` is in the system path'
    ' * The path to the docker-credentials-* tool is valid'
    ' * That the `docker` CLI tool is logged into Docker Hub with the relevant credentials.'
    ' * That the Climber Docker image has been downloaded from Docker Hub.' 
    """
    # ' * That `docker` is in the system path'
    _check_docker_is_in_sys_path()

    # ' * The path to the docker-credentials-* tool is valid'
    _check_docker_credentials_tool_exists(cli_defaults, cli_config_fname)

    # ' * That the `docker` CLI tool is logged into Docker Hub with the relevant credentials.'
    _check_logged_into_docker_hub(cli_defaults, cli_config_fname)

    # ' * That the Climber Docker image has been downloaded from Docker Hub.' 
    _check_climber_docker_image_is_downloaded(cli_defaults, cli_config_fname)


def _check_docker_is_in_sys_path():
    try:
        subprocess.call('docker')
        print('Succesfully found `docker` command in shell path')
    except (OSError):
        raise ValueError('ERROR: Docker is not installed and available in the system path on this computer')


def _check_docker_credentials_tool_exists(cli_defaults, cli_config_fname):
    cred_tool_fpath = cli_defaults.get('climber', 'docker_credentials')
    if path.exists(cred_tool_fpath):
        print('Found Docker Credentials Tool at\n\t{0}'.format(cred_tool_fpath))
    else:
        raise ValueError('ERROR: The Docker Credentials Tool cannot be found at:\n\t{0}\n'
                         'Please either install docker in the default location'
                         ' or update {1} with the correct path for your computer.'.format(
                            cred_tool_fpath,
                            cli_config_fname
                         ))


def _check_logged_into_docker_hub(cli_defaults, cli_config_fname):
    cred_tool_fpath = cli_defaults.get('climber', 'docker_credentials')
    docker_username = cli_defaults.get('climber', 'docker_username')

    # cread_list_str = subprocess.check_output('{} list'.format(cred_tool_fpath))
    cread_list_str = subprocess.check_output([cred_tool_fpath, 'list'])
    
    if re.search(docker_username, ':"{}"'.format(cread_list_str)):
        print('Logged into Docker Hub as user `{}`'.format(docker_username))
        return

    raise ValueError('ERROR: Not logged into Docker Hub as user `{0}`\n'
                     'To rectify either:\n'
                     'a) Update `{1}` with the desired username\n'
                     'b) Login to Docker Hub using the command: `docker login`.'
                     ' Use "docker login --help" for more information.'
                     ''.format(docker_username, cli_config_fname))



    ' * That the Climber Docker image has been downloaded from Docker Hub.' 
def _check_climber_docker_image_is_downloaded(cli_defaults, cli_config_fname):
    pass



def launch_climber(cli_defaults):
    print('Launch Climber here....')