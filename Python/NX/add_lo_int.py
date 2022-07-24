from netmiko import ConnectHandler
from getpass import getpass

router = { 
    "device_type": "cisco_nxos",
    "ip": "sandbox-nxos-1.cisco.com",
    "username": "admin",
    "password": "Admin_1234!"
}

commands = ["int l300",
            "desc pytest",
            "ip add 1.1.255.255 255.255.255.255", 
            "do sh ip int br"]

with ConnectHandler(**router) as net_connect:
    output = net_connect.send_config_set(commands) 

print("\n\n")
print("*"*20)
print(output)
print("*"*20)
print("\n\n")