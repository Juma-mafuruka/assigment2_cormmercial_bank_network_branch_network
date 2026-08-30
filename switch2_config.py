from netmiko import ConnectHandler

sw2_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5006,
    'fast_cli': False,  # Inazuia Netmiko kuharakisha amri kupita kiasi
}

sw2_commands = [
    'vlan 11',
    'name CustomerService',
    'exit',
    'vlan 21',
    'name Administration',
    'exit',
    'interface GigabitEthernet0/1',
    'switchport mode trunk',
    'switchport trunk allowed vlan 11,21',
    'no shutdown',
    'exit',
    'interface GigabitEthernet0/2',
    'switchport mode access',
    'switchport access vlan 11',
    'no shutdown',
    'exit',
    'interface GigabitEthernet0/3',
    'switchport mode access',
    'switchport access vlan 21',
    'no shutdown',
    'exit'
]

print("=== INAANZA KU-CONFIGURE SWITCH SW2 ===\n")

try:
    net_connect = ConnectHandler(**sw2_device)
    
    # Hakikisha kifaa kipo kwenye privileged mode (SW2#)
    net_connect.write_channel("\r\n")
    net_connect.enable()
    
    output = net_connect.send_config_set(sw2_commands)
    print(output)
    
    net_connect.disconnect()
    print("\n=== CONFIGURATION YA SW2 IMEKAMILIKA ===")

except Exception as e:
    print(f"Kuna tatizo wakati wa kuunganisha SW2: {e}")
