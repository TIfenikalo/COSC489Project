from utils import run_command

def scan_for_aps():
    print("Step 3: Scanning for Access Points. Close when you find your target (CTRL+C)...")
    run_command("sudo airodump-ng wlan0")
