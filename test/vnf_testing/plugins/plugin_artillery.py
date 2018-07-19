# -*- coding: utf-8 -*-
# plugin_artillery.py

from ssh_manager import listener
import subprocess
import logging
LOG = logging.getLogger(__name__)


# Bash Command Function for using bash shell
def bash_command(cmd):
    subprocess.Popen(['/bin/bash', '-c', cmd])


def start(hosts=None, auth=None, vnf_testing_args_dict=None):
    """Starts artillery tool.

    Args:
        hosts: A host's ip that user wants to test in.
        auth: A host's password or publickey that user wants to test in.
        vnf_testing_args_dict: A dictionary of arguments used to execute the vnf testing plugins.

    Returns:
        None.
    """
    cmd = 'artillery quick --count 10 -n 20 http://192.168.8.101/'
    # cmd = 'artillery run artillery_config.yml'
    # artillery_config.yml transfer needed
    # vnf_testing_args_dict has the path of artillery_config.yml
    listener.start_command(hosts=hosts, auth=auth, command=cmd)
