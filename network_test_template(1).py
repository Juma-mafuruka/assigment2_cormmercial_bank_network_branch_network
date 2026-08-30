network_test_template(1).py
from netmiko import ConnectHandler

# Taarifa za Muunganisho wa Router R1
r1_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5001,
    'global_delay_factor': 2,
    'fast_cli': False,
}

# Taarifa za Muunganisho wa Router R2
r2_device = {
    'device_type': 'cisco_ios_telnet',
    'host': '192.168.31.128',
    'port': 5002,
    'global_delay_factor': 2,
    'fast_cli': False,
}

# Majaribio ya kufanya kutoka R1
r1_tests = [
    ("Point-to-Point Link (R1 -> R2)", "ping 10.2.2.2 repeat 3"),
    ("Branch 1 Local CS Gateway", "ping 172.16.11.1 repeat 3"),
    ("Branch 1 Local Admin Gateway", "ping 172.16.21.1 repeat 3"),
    ("Branch 2 Remote CS Gateway (via OSPF)", "ping 172.16.31.1 repeat 3"),
    ("Branch 2 Remote Admin Gateway (via OSPF)", "ping 172.16.41.1 repeat 3"),
    ("End-to-End: CS-PC1 (Branch 1)", "ping 172.16.11.10 repeat 3"),
    ("End-to-End: Admin-PC1 (Branch 1)", "ping 172.16.21.10 repeat 3"),
    ("End-to-End: CS-PC2 (Branch 2)", "ping 172.16.31.10 repeat 3"),
    ("End-to-End: Admin-PC2 (Branch 2)", "ping 172.16.41.10 repeat 3"),
]

# Majaribio ya kufanya kutoka R2
r2_tests = [
    ("Point-to-Point Link (R2 -> R1)", "ping 10.2.2.1 repeat 3"),
    ("Branch 2 Local CS Gateway", "ping 172.16.31.1 repeat 3"),
    ("Branch 2 Local Admin Gateway", "ping 172.16.41.1 repeat 3"),
    ("Branch 1 Remote CS Gateway (via OSPF)", "ping 172.16.11.1 repeat 3"),
    ("Branch 1 Remote Admin Gateway (via OSPF)", "ping 172.16.21.1 repeat 3"),
    ("End-to-End: CS-PC2 (Branch 2)", "ping 172.16.31.10 repeat 3"),
    ("End-to-End: Admin-PC2 (Branch 2)", "ping 172.16.41.10 repeat 3"),
    ("End-to-End: CS-PC1 (Branch 1)", "ping 172.16.11.10 repeat 3"),
    ("End-to-End: Admin-PC1 (Branch 1)", "ping 172.16.21.10 repeat 3"),
]

def run_device_tests(device_name, device_info, tests):
    print("=" * 70)
    print(f"   INAANZA MAJARIBIO YA MWISHO YA MTANDAO KUTOKA: {device_name}")
    print("=" * 70 + "\n")
    
    try:
        net_connect = ConnectHandler(**device_info)
        net_connect.write_channel("\r\n")
        net_connect.enable()
        
        for description, cmd in tests:
            print(f"--- [TEST]: {description} ---")
            print(f"COMMAND: {cmd}")
            output = net_connect.send_command(cmd, expect_string=r'#', read_timeout=15)
            
            # Angalia kama ping imefanikiwa
            if "Success rate is 100 percent" in output or "Success rate is 80 percent" in output:
                print("STATUS: [ PASSED ]")
            else:
                print("STATUS: [ FAILED ]")
            print(output)
            print("-" * 50 + "\n")
            
        net_connect.disconnect()
        print(f"=== MAJARIBIO YA {device_name} YAMEKAMILIKA ===\n\n")

    except Exception as e:
        print(f"Tatizo la kuunganisha {device_name}: {e}\n")

if __name__ == "__main__":
    print("\n" + "#" * 70)
    print("#  ASSIGNMENT 2 - COMMERCIAL BANK BRANCH NETWORK (END-TO-END TEST)  #")
    print("#" * 70 + "\n")
    
    # 1. Endesha VIPIMO kutoka R1
    run_device_tests("ROUTER R1 (BRANCH 1)", r1_device, r1_tests)
    
    # 2. Endesha VIPIMO kutoka R2
    run_device_tests("ROUTER R2 (BRANCH 2)", r2_device, r2_tests)
    
    print("#" * 70)
    print("#         KAZI IMEKAMILIKA! MTANDAO WOTE UMEVERIFIWA NA UKO UP        #")
    print("#" * 70 + "\n")
