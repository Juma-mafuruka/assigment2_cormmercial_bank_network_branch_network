from netmiko import ConnectHandler

r2_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5002,
    'fast_cli': False,
}

verification_commands = [
    # 1. Kuangalia hali ya Sub-interfaces na IP addresses
    'show ip interface brief',
    
    # 2. Kuangalia kama OSPF Adjacency na R1 ipo FULL
    'show ip ospf neighbor',
    
    # 3. Kuangalia Routing Table ili kuthibitisha kama OSPF imejifunza Branch 1 routes
    'show ip route ospf'
]

print("=== INAANZA KUVERIFY ROUTER R2 ===\n")

try:
    net_connect = ConnectHandler(**r2_device)
    net_connect.write_channel("\r\n")
    net_connect.enable()
    
    for cmd in verification_commands:
        print("=" * 60)
        print(f"COMMAND: {cmd}")
        print("=" * 60)
        output = net_connect.send_command(cmd)
        print(output)
        print("\n")

    net_connect.disconnect()
    print("=== VERIFICATION YA R2 IMEKAMILIKA ===")

except Exception as e:
    print(f"Tatizo wakati wa kuunganisha R2: {e}")
