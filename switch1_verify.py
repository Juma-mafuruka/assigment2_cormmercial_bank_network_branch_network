from netmiko import ConnectHandler

sw1_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5004,
}

verification_commands = [
    # 1. Kuangalia kama VLAN 11 na VLAN 21 zimeundwa na zipo active
    'show vlan brief',
    
    # 2. Kuangalia uunganisho wa Trunk kwenye Gi0/1 na VLANs zilizoruhusiwa (11,21)
    'show interface trunk',
    
    # 3. Kuangalia hali ya ports zote (Gi0/1, Gi0/2, Gi0/3)
    'show interface status'
]

print("=== INAANZA KUVERIFY SWITCH SW1 ===\n")

try:
    net_connect = ConnectHandler(**sw1_device)
    
    for cmd in verification_commands:
        print("=" * 60)
        print(f"COMMAND: {cmd}")
        print("=" * 60)
        output = net_connect.send_command(cmd)
        print(output)
        print("\n")

    net_connect.disconnect()
    print("=== VERIFICATION YA SW1 IMEKAMILIKA ===")

except Exception as e:
    print(f"Kuna tatizo wakati wa kuunganisha SW1: {e}")
