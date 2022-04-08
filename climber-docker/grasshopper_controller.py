
import ConfigParser
from os import path, chdir
import subprocess

def check_grasshopper_globals(cli_defaults, cli_config_fname):
    """
    ' * That the `cli_defaults.cfg` file exists and can be loaded.'
    ' * The path to the Rhino.exe is valid'
    ' * The path to the Grasshopper (`.gh`) file is valid'
    """
    # That the `cli_defaults.cfg` file exists and can be loaded.'
    # try:
    #     cli_defaults = read_cli_defaults_file()
    # except IOError:
    #     raise ValueError('The file could not be found')
    # except ConfigParser.Error:
    #     raise ValueError('There was a problem with reading then contents of the file')

    # The path to the Rhino.exe is valid'
    rhino_fname = cli_defaults.get('rhino_grasshopper', 'rhino_exe_fname')
    rhino_dir = cli_defaults.get('rhino_grasshopper', 'rhino_dir')
    rhino_fpath = path.join(rhino_dir, rhino_fname)
    if path.exists(rhino_fpath):
        print('Found Rhino exe at:\n\t{0}'.format(rhino_fpath))
    else:
        raise ValueError('ERROR: Rhino cannot be found in the found at:\n\t{0}\n'
                         'Please either install Rhino7 in the default location'
                         ' or update {1} with the correct path to Rhino for your computer.'.format(
                            rhino_fpath,
                            cli_config_fname
                         ))

    # The path to the Grasshopper (`.gh`) file is valid'
    grasshopper_fname = cli_defaults.get('rhino_grasshopper', 'grasshopper_file')
    grasshopper_fpath = path.join(path.dirname(path.realpath(__file__)), grasshopper_fname)
    if path.exists(grasshopper_fpath):
        print('Found Grasshopper file at\n\t{0}'.format(grasshopper_fpath))
    else:
        raise ValueError('ERROR: The Grasshopper file (`.gh`) cannot be found at:\n\t{0}\n'
                         'Please either place the grasshopper file in the specified location'
                         ' or update {1} with the correct path for your computer.'.format(
                            grasshopper_fpath,
                            cli_config_fname
                         ))


def launch_grasshopper(cli_defaults):
    """
    Launches the Grasshopper instance. Runs (plays) the grasshopper file then exits.
    """

    # Work out some parameter values:
    rhino_fname = cli_defaults.get('rhino_grasshopper', 'rhino_exe_fname')
    rhino_dir = cli_defaults.get('rhino_grasshopper', 'rhino_dir')
    rhino_fpath = path.join(rhino_dir, rhino_fname)
    grasshopper_fname = cli_defaults.get('rhino_grasshopper', 'grasshopper_file')
    grasshopper_fpath = path.join(path.dirname(path.realpath(__file__)), grasshopper_fname)

    # Create the full commandline as a string.
    # 
    # This approach is used, because attempting to rely on the automatic formatting of 
    # passing a list of args to `subprocess.call_output` does not play nicely with the 
    # `runscript` value.
    #
    # The final string should look like (using GrasshopperPlayer):
    # ```
    # c:\Program Files\Rhino 7\System\Rhino.exe"  /nosplash /runscript="-GrasshopperPlayer 
    # C:\Users\proteins\protein_folding\climber-docker\gh_loop_with_cli.gh _Exit" /notemplate
    # ```
    # For some unknown reason the GrasshopperPlayer quits before exporting the PBD file
    # full_cmd = '"{}" /nosplash /runscript="-GrasshopperPlayer {} _Exit" /notemplate'.format(
    #     rhino_fpath,
    #     grasshopper_fpath
    # )
    #
    # The final string should look like (using Grasshopper):
    # ```
    # c:\Program Files\Rhino 7\System\Rhino.exe"  /nosplash /runscript="-Grasshopper 
    # editor load document open C:\Users\proteins\protein_folding\climber-docker\gh_loop_with_cli.gh _enter" /notemplate
    # ```
    # Ideally the command should include `_exit Yes` to quite after completing. However this fails if there are
    # any open error messages or dialog boxes.
    # full_cmd = '"{}" /nosplash /runscript="-Grasshopper editor load document open {} _enter _Exit Yes" /notemplate'.format(
    #     rhino_fpath,
    #     grasshopper_fpath
    # )
    # Therefore using this command for now
    full_cmd = '"{}" /nosplash /runscript="-Grasshopper editor load document open {} _enter" /notemplate'.format(
        rhino_fpath,
        grasshopper_fpath
    )

    # Now lauch Rhino itself
    # chdir(rhino_dir)
    rhino_output = subprocess.check_output(full_cmd, shell=False)
    print('rhino_output=\n')
    print(rhino_output)
    print('\nDONE')
