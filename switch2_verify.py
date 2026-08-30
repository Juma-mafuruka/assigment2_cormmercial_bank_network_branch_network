from netmiko import ConnectHandler

sw2_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5006,
    'fast_cli': False,
}

verification_commands = [
    # 1. Kuangalia kama VLAN 11 (CustomerService) na VLAN 21 (Administration) zipo active
    'show vlan brief',
    
    # 2. Kuangalia uunganisho wa Trunk kwenye Gi0/1 na VLANs zilizoruhusiwa (11,21)
    'show interface trunk',
    
    # 3. Kuangalia hali ya ports na VLAN assignment (Gi0/2 -> VLAN 11, Gi0/3 -> VLAN 21)
    'show interface status'
]

print("=== INAANZA KUVERIFY SWITCH SW2 ===\n")

try:
    net_connect = ConnectHandler(**sw2_device)
    
    # Hakikisha kifaa kipo kwenye privileged mode (SW2#)
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
    print("=== VERIFICATION YA SW2 IMEKAMILIKA ===")

except Exception as e:
    print(f"Kuna tatizo wakati wa kuunganisha SW2: {e}")
