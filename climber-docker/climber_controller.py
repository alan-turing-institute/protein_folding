
from operator import contains
from os import path, devnull, chdir
from posixpath import join as posixjoin
import subprocess
import re
# from icecream import ic
from time import sleep
from run_loop import get_host_shared_dir_path

_climber_container_name = "climber_app_latest"

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
    climber_image_name = cli_defaults.get('climber', 'docker_image_name')
    climber_image_ver = cli_defaults.get('climber', 'docker_image_ver')

    re_search_str = "^{}\s+{}".format(re.escape(climber_image_name), re.escape(climber_image_ver))

    cmd_str = 'docker images'
    images_str = _run_docker_sync(cmd_str)
    # print('re_search_str=', re_search_str)
    # print('images_str=', images_str)

    image_found = re.search(re_search_str, images_str, re.MULTILINE|re.IGNORECASE)
    # print('image_found=', image_found)
    if image_found:
        print("Docker image `{}:{}` found locally.".format(climber_image_name, climber_image_ver))
        return

    raise ValueError('ERROR: Required version of Climber docker image not found locally. Please download'
                     ' manually using `docker pull` command, or using the `--pull-docker-image` switch.')


def pull_climber_docker_image(cli_defaults):
    climber_image_name = cli_defaults.get('climber', 'docker_image_name')
    climber_image_ver = cli_defaults.get('climber', 'docker_image_ver')

    cmd_str = 'docker pull {}:{}'.format(climber_image_name, climber_image_ver)
    _run_docker_sync(cmd_str)


def launch_climber(cli_defaults):
    print('Launch Climber here....')
    shared_dir_name = cli_defaults.get('shared', 'shared_dir')
    climber_image_name = cli_defaults.get('climber', 'docker_image_name')
    climber_image_ver = cli_defaults.get('climber', 'docker_image_ver')

    host_shared_dir_path = get_host_shared_dir_path(cli_defaults)
    image_shared_path = posixjoin("/usr/src/Climber/examples", shared_dir_name)

    # `cd usr/src/Climber/examples/RUN101`
    # `python3 climberrunner.py`
    # cmd = ('docker run --rm --detach -v {0}:{1} -it --name {2} {3}:{4} bash -c "cd {1}; python3 climberrunner.py"'.format(
    #            host_shared_dir_path,
    #            image_shared_path,
    #            _climber_container_name,
    #            climber_image_name,
    #            climber_image_ver))

    cmd = ('docker run --detach --rm -v {0}:{1} -it {3}:{4} bash -c "cd {1}; python3 climberrunner.py"'.format(
               host_shared_dir_path,
               image_shared_path,
               _climber_container_name,
               climber_image_name,
               climber_image_ver))

    print('launch_climber_cmd=', cmd)
    # return _run_docker_background(cmd)
    # return _run_docker_sync(cmd)
    # output = _run_docker_sync(cmd)
    output = subprocess.check_output(cmd)
    print(output)
    return output

def _run_docker_sync(cmd_str):
    """
    Runs a docker command synchronisly.
    returns the exit code of the command
    """
    # ic(cmd_str)
    cmd_ary = cmd_str.split()
    # subprocess.run(cmd_ary, check=True)

    cmd_output = subprocess.check_output(cmd_ary)
    # ic(cmd_output)
    return cmd_output


def _run_docker_background(cmd_str):
    """
    Runs a docker command synchronisly.
    returns the CONTAINER ID
    """
    # `-d` arg
    # ic(cmd_str)
    if (" -d " not in cmd_str) and ("--detach" not in cmd_str):
        raise ValueError(
            "Docker command called as background process, but does not include the `--detach/-d` switch. Command=`{cmd_str}"
        )

    return _run_docker_sync(cmd_str)

    # # completed_process = subprocess.run(cmd_ary, check=True)
    # # # Allow at five secounds for the Docker instance to start
    # # sleep(5)
    # # completed_process.check_returncode()
    # # self._container_id = completed_process.stdout
    # # ic(self._container_id)

    # container_id = subprocess.check_output(cmd_ary)
    # ic(container_id)
    # return container_id


def stop_background_docker(container_id):
    cmd_stop = "docker stop {}".format(container_id)
    _run_docker_sync(cmd_stop)
