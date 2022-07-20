from netmiko import ConnectHandler
from getpass import getpass

r_two = { 
    "device_type": "cisco_ios",
    "ip": "192.168.122.12",
    "username": "cisco2",
    "password": getpass(), # getpass for asking password when run py file. make secure than hardcode password on a file
}

commands = ["int g0/1", 
            "ip add 10.0.1.1 255.255.255.252", 
            "no sh", 
            "do sh ip int br"]

with ConnectHandler(**r_two) as net_connect:
    output = net_connect.send_config_set(commands) # config_set for send multi commands

print("\n\n")
print("*"*20)
print(output)
print("*"*20)

