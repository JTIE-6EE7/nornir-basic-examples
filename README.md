# Nornir basic examples

Simple examples demonstrating Nornir basics

## Inventory

hosts.yaml contains all the devices Nornir will run against

defaults.yaml contains the username, password and platform to be used by Netmiko

## nr-run-command.py

nr-run_command.py imports only the needed modules, defines a task to execute the command
found in "command_string" and runs that task against all devices found in inventory.

## nr-host-data.py

nr-host-data.py demonstrates assigning and accessing data with host variables
