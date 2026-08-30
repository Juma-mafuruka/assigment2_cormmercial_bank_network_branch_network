from netmiko import ConnectHandler

r1_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5000,
}

r1_commands = [
    'interface GigabitEthernet0/0',
    'no shutdown',
    'exit',
    'interface GigabitEthernet0/0.11',
    'encapsulation dot1Q 11',
    'ip address 172.16.11.1 255.255.255.0',
    'exit',
    'interface GigabitEthernet0/0.21',
    'encapsulation dot1Q 21',
    'ip address 172.16.21.1 255.255.255.0',
    'exit',
    'interface GigabitEthernet0/1',
    'ip address 10.2.2.1 255.255.255.252',
    'no shutdown',
    'exit',
    'router ospf 1',
    'router-id 1.1.1.1',
    'network 172.16.11.0 0.0.0.255 area 0',
    'network 172.16.21.0 0.0.0.255 area 0',
    'network 10.2.2.0 0.0.0.3 area 0',
    'exit'
]

print("Inaconfigure R1...")
net_connect = ConnectHandler(**r1_device)
output = net_connect.send_config_set(r1_commands)
print(output)
net_connect.disconnect()
print("R1 imekamilika!")
