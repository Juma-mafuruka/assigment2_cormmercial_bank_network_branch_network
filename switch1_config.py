from netmiko import ConnectHandler

# Mipangilio ya kuunganisha SW1 kupitia GNS3 Telnet Port 5004
sw1_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5004,
}

# Amri za ku-configure SW1
sw1_commands = [
    # 1. Kutengeneza VLANs na kutoa majina
    'vlan 11',
    'name CustomerService',
    'exit',
    'vlan 21',
    'name Administration',
    'exit',
    
    # 2. Kuweka Port Gi0/1 kuwa Trunk kuelekea Router R1
    'interface GigabitEthernet0/1',
    'switchport mode trunk',
    'switchport trunk allowed vlan 11,21',
    'no shutdown',
    'exit',
    
    # 3. Kuweka Port Gi0/2 kuwa Access Port ya CS-PC1 (VLAN 11)
    'interface GigabitEthernet0/2',
    'switchport mode access',
    'switchport access vlan 11',
    'no shutdown',
    'exit',
    
    # 4. Kuweka Port Gi0/3 kuwa Access Port ya Admin-PC1 (VLAN 21)
    'interface GigabitEthernet0/3',
    'switchport mode access',
    'switchport access vlan 21',
    'no shutdown',
    'exit'
]

print("=== INAANZA KU-CONFIGURE SWITCH SW1 ===\n")

try:
    net_connect = ConnectHandler(**sw1_device)
    output = net_connect.send_config_set(sw1_commands)
    print(output)
    net_connect.disconnect()
    print("\n=== CONFIGURATION YA SW1 IMEKAMILIKA ===")

except Exception as e:
    print(f"Kuna tatizo wakati wa kuunganisha SW1: {e}")
