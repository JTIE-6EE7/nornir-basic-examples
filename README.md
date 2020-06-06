# nr-run_command.py

Simple example of running a command on network devices and printing the output


Sample output:

vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO

Interface              IP-Address      OK? Method Status                Protocol

GigabitEthernet1       172.20.12.2     YES TFTP   up                    up

GigabitEthernet2       172.20.23.2     YES TFTP   up                    up

GigabitEthernet0       172.20.58.32    YES NVRAM  up                    up

Loopback0              2.2.2.2         YES TFTP   up                    up

^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       172.20.12.1     YES TFTP   up                    up
GigabitEthernet2       172.20.13.1     YES TFTP   up                    up
GigabitEthernet0       172.20.58.31    YES NVRAM  up                    up
Loopback0              1.1.1.1         YES TFTP   up                    up
^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
vvvv netmiko_send_command ** changed : False vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv INFO
Interface              IP-Address      OK? Method Status                Protocol
GigabitEthernet1       172.20.13.3     YES TFTP   up                    up
GigabitEthernet2       172.20.23.3     YES TFTP   up                    up
GigabitEthernet0       172.20.58.33    YES NVRAM  up                    up
Loopback0              3.3.3.3         YES TFTP   up                    up
^^^^ END netmiko_send_command ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
