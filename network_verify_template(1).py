from netmiko import ConnectHandler

devices = [
    {
        'name': 'ROUTER R1 (Branch 1)',
        'info': {
            'device_type': 'cisco_ios_telnet',
            'host': '192.168.31.128',
            'port': 5000,  # Sahihi kutoka GNS3
            'fast_cli': False,
        },
        'commands': [
            'show ip interface brief',
            'show ip ospf neighbor',
            'show ip route ospf'
        ]
    },
    {
        'name': 'ROUTER R2 (Branch 2)',
        'info': {
            'device_type': 'cisco_ios_telnet',
            'host': '192.168.31.128',
            'port': 5002,  # Sahihi kutoka GNS3
            'fast_cli': False,
        },
        'commands': [
            'show ip interface brief',
            'show ip ospf neighbor',
            'show ip route ospf'
        ]
    },
    {
        'name': 'SWITCH SW1 (Branch 1)',
        'info': {
            'device_type': 'cisco_ios_telnet',
            'host': '192.168.31.128',
            'port': 5004,  # Sahihi kutoka GNS3
            'fast_cli': False,
        },
        'commands': [
            'show vlan brief',
            'show interfaces trunk'
        ]
    },
    {
        'name': 'SWITCH SW2 (Branch 2)',
        'info': {
            'device_type': 'cisco_ios_telnet',
            'host': '192.168.31.128',
            'port': 5006,  # Sahihi kutoka GNS3
            'fast_cli': False,
        },
        'commands': [
            'show vlan brief',
            'show interfaces trunk'
        ]
    }
]

print("\n" + "=" * 70)
print("===   INAANZA KU-VERIFY MTANDAO MZIMA (R1, R2, SW1, SW2)   ===")
print("=" * 70 + "\n")

for dev in devices:
    print("#" * 60)
    print(f"   VERIFYING: {dev['name']}")
    print("#" * 60)
    
    try:
        net_connect = ConnectHandler(**dev['info'])
        net_connect.write_channel("\r\n")
        net_connect.enable()
        
        for cmd in dev['commands']:
            print("\n" + "-" * 50)
            print(f"COMMAND: {cmd}")
            print("-" * 50)
            output = net_connect.send_command(cmd)
            print(output)
            
        net_connect.disconnect()
        print(f"\n>>> Verification ya {dev['name']} IMEKAMILIKA <<<\n\n")

    except Exception as e:
        print(f"\n[X] Tatizo la kuunganisha na {dev['name']}: {e}\n\n")

print("=" * 70)
print("===         VERIFICATION YA MTANDAO MZIMA IMEKAMILIKA!         ===")
print("=" * 70 + "\n")
