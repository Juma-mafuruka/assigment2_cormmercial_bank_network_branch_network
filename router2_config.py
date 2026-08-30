from netmiko import ConnectHandler

r2_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5002,
    'fast_cli': False,
}

r2_fix_commands = [
    # 1. Ondoa IP zilizowekwa makosa kwenye Gi0/2 na Gi0/3
    'interface GigabitEthernet0/2',
    'no ip address',
    'shutdown',
    'exit',
    'interface GigabitEthernet0/3',
    'no ip address',
    'shutdown',
    'exit',
    
    # 2. Washa Main Interface ya LAN
    'interface GigabitEthernet0/0',
    'no shutdown',
    'exit',
    
    # 3. Weka IP kwenye Sub-interface 11 (VLAN 11)
    'interface GigabitEthernet0/0.11',
    'encapsulation dot1Q 11',
    'ip address 172.16.31.1 255.255.255.0',
    'no shutdown',
    'exit',
    
    # 4. Weka IP kwenye Sub-interface 21 (VLAN 21)
    'interface GigabitEthernet0/0.21',
    'encapsulation dot1Q 21',
    'ip address 172.16.41.1 255.255.255.0',
    'no shutdown',
    'exit',
    
    # 5. Hakikisha Point-to-Point Link ipo sawa
    'interface GigabitEthernet0/1',
    'ip address 10.2.2.2 255.255.255.252',
    'no shutdown',
    'exit',
    
    # 6. Tangaza mitandao kwenye OSPF
    'router ospf 1',
    'router-id 2.2.2.2',
    'network 172.16.31.0 0.0.0.255 area 0',
    'network 172.16.41.0 0.0.0.255 area 0',
    'network 10.2.2.0 0.0.0.3 area 0',
    'exit'
]

print("=== INAREKEBISHA CONFIGURATION YA R2 ===\n")

try:
    net_connect = ConnectHandler(**r2_device)
    net_connect.write_channel("\r\n")
    net_connect.enable()
    
    output = net_connect.send_config_set(r2_fix_commands)
    print(output)
    
    net_connect.disconnect()
    print("\n=== MAREKEBISHO YA R2 YAMEKAMILIKA ===")

except Exception as e:
    print(f"Tatizo wakati wa kuunganisha R2: {e}")
