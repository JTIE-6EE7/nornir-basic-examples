#!/usr/local/bin/python3

"""
This script is used to run a command on network devices with Nornir
"""

from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


def run_command(task):
    # command to be run
    cmd = "show ip interface brief | i Loop"
    # send command to device
    output = task.run(
        task=netmiko_send_command, 
        command_string=cmd
    )
    # assign output to host variable
    task.host["version"] = output.result

def print_version(task):
    # print inventory hostname
    print(task.host)
    # print previously assigned output
    print(task.host["version"])
    print()

def main():
    # initialize The Norn
    nr = InitNornir()
    # run The Norn to run command
    nr.run(task=run_command)
    # print results for each host
    nr.run(task=print_version)
   

if __name__ == "__main__":
    main()
