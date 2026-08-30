from netmiko import ConnectHandler

r1_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5000,
    'global_delay_factor': 2,
}

test_commands = [
    # --- 1. VIPIMO VYA R1 KWENDA R2 ---
    # Kuangalia hali ya interface inayounga R1 na R2 (Gi0/1)
    'show interface GigabitEthernet0/1 brief',
    # Ping R2 Point-to-Point Link IP (10.2.2.2)
    'ping 10.2.2.2 repeat 5',
    # Kuangalia OSPF Neighbor Status na R2
    'show ip ospf neighbor',
    
    # --- 2. VIPIMO VYA R1 KWENDA SW1 ---
    # Kuangalia hali ya Sub-interfaces zinazounganisha R1 na SW1 Trunk link (Gi0/0.11 na Gi0/0.21)
    'show ip interface GigabitEthernet0/0.11 brief',
    'show ip interface GigabitEthernet0/0.21 brief',
    # Ping Gateway IPs za R1 zenyewe zilizopo kwenye Trunk Link kuelekea SW1
    'ping 172.16.11.1 repeat 3',
    'ping 172.16.21.1 repeat 3'
]

print("=== INAANZA KU-TEST R1 -> R2 NA R1 -> SW1 ===\n")

try:
    net_connect = ConnectHandler(**r1_device)
    net_connect.write_channel("\r\n")
    net_connect.enable()
    
    for cmd in test_commands:
        print("=" * 65)
        print(f"COMMAND: {cmd}")
        print("=" * 65)
        
        if 'ping' in cmd:
            output = net_connect.send_command(cmd, expect_string=r'R1#', read_timeout=15)
        else:
            output = net_connect.send_command(cmd)
            
        print(output)
        print("\n")

    net_connect.disconnect()
    print("=== MAJARIBIO YA R1 YAMEKAMILIKA ===")

except Exception as e:
    print(f"Kuna tatizo wakati wa kuunganisha R1: {e}")
