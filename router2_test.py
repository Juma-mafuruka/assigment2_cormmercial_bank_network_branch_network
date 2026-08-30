from netmiko import ConnectHandler

r2_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5002,
    'global_delay_factor': 2,
    'fast_cli': False,
}

test_commands = [
    # 1. Test mawasiliano ya Router-to-Router (R2 -> R1)
    'ping 10.2.2.1 repeat 5',
    
    # 2. Test Local Sub-interfaces/Gateways za Branch 2 (R2 -> SW2)
    'ping 172.16.31.1 repeat 3',  # CustomerService Gateway
    'ping 172.16.41.1 repeat 3',  # Administration Gateway
    
    # 3. Test Remote Gateways za Branch 1 kupitia OSPF
    'ping 172.16.11.1 repeat 3',  # Branch 1 CS Gateway
    'ping 172.16.21.1 repeat 3',  # Branch 1 Admin Gateway
    
    # 4. Test Connectivity kwenda kwa End-User VPCS
    'ping 172.16.31.10 repeat 5', # CS-PC2
    'ping 172.16.41.10 repeat 5'  # Admin-PC2
]

print("=== INAANZA KU-TEST ROUTER R2 ===\n")

try:
    net_connect = ConnectHandler(**r2_device)
    net_connect.write_channel("\r\n")
    net_connect.enable()
    
    for cmd in test_commands:
        print("=" * 65)
        print(f"COMMAND: {cmd}")
        print("=" * 65)
        output = net_connect.send_command(cmd, expect_string=r'R2#', read_timeout=15)
        print(output)
        print("\n")

    net_connect.disconnect()
    print("=== TESTING YA R2 IMEKAMILIKA ===")

except Exception as e:
    print(f"Tatizo wakati wa kuunganisha R2: {e}")
