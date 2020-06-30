# nr-run_command.py

Simple example of running a command on network devices and printing the output


hosts.yaml contains all the devices Nornir will run against

defaults.yaml contains the username, password and platform to be used by Netmiko

nr-run_command.py imports only the needed modules, defines a task to execute the command
found in "command_string" and runs that task against all devices found in inventory.
