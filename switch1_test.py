from netmiko import ConnectHandler
from netmiko.exceptions import (
    NetmikoTimeoutException,
    NetmikoAuthenticationException,
)

# Start the switch in GNS3 before running this script.
# Enter the connection details of the switch from which
# the network tests will be performed.
switch = {
    "device_type": "cisco_ios_telnet",
    "host": "192.168.31.128",
    "username": "",
    "password": "",
    "secret": "12345678",
    "port": "5004",
}


# Enter the operational tests required for the provided network.
testing_commands = [

    # Verify that the switch has learned MAC addresses.
   #Verify VLAN 11 CustomerService exists, 
   "show vlan id 11",
    #Verify VLAN 21 Admin exists, 
    "show vlan id 21",
    #Verify trunk to R1, 
    "show interfaces GigabitEthernet0/1 switchport",
    #Verify learned MAC addresses, 
    "show mac address-table",

    
]


connection = None

try:
    # Connect to the switch through its GNS3 TELNET console.
    connection = ConnectHandler(**switch)

    # Enter privileged EXEC mode if an enable password is configured.
    if switch["secret"]:
        connection.enable()

    # Run each test command and display its result.
    for command in testing_commands:
        print(f"\n--- Testing: {command} ---")

        output = connection.send_command(
            command,
            read_timeout=30
        )

        print(output)

    print("\nSwitch testing completed.")


except NetmikoTimeoutException:
    print(
        "Connection timed out. Check the GNS3 VM IP address, "
        "TELNET console port, GNS3 VM, and switch state."
    )


except NetmikoAuthenticationException:
    print(
        "Authentication failed. Check the username, password, "
        "and enable password."
    )


except Exception as error:
    print(f"Unexpected error: {error}")


finally:
    # Close the TELNET connection if it was opened successfully.
    if connection is not None:
        connection.disconnect()
