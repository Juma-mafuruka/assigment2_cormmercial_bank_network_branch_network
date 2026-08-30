from netmiko import ConnectHandler

r1_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5000,
    'global_delay_factor': 2,
}

# Amri za ku-verify R1 pekee bila kutegemea R2
local_verification_commands = [
    # 1. Kuangalia Hali ya Interface na Sub-interfaces
    'show ip interface brief',
    
    # 2. Kuangalia IP routing table ya ndani ya R1 (Connected routes)
    'show ip route connected',
    
    # 3. Kuangalia kama OSPF imewezeshwa kwenye R1
    'show ip ospf interface brief',
    
    # 4. Ku-ping IP za Sub-interfaces za R1 zenyewe (Self-ping test)
    'ping 172.16.11.1',
    'ping 172.16.21.1',
    'ping 10.2.2.1',
    
    # 5. Ku-ping CS-PC1 na Admin-PC1 (kama zimeshawekwa IP kwenye GNS3)
    'ping 172.16.11.10',
    'ping 172.16.21.10'
]

print("=== INAANZA LOCAL VERIFICATION YA R1 ===\n")

try:
    net_connect = ConnectHandler(**r1_device)
    
    for cmd in local_verification_commands:
        print("=" * 60)
        print(f"COMMAND: {cmd}")
        print("=" * 60)
        
        if 'ping' in cmd:
            output = net_connect.send_command(cmd, expect_string=r'R1#', read_timeout=15)
        else:
            output = net_connect.send_command(cmd)
            
        print(output)
        print("\n")

    net_connect.disconnect()
    print("=== LOCAL VERIFICATION YA R1 IMEKAMILIKA ===")

except Exception as e:
    print(f"Kuna tatizo wakati wa kuunganisha R1: {e}")
