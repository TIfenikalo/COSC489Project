#in charge of changing the wlan0 into monitor mode
from utils import run_command

def start_monitor():
    print("Step 1: Killing processes that may interfere...")
    run_command("sudo airmon-ng check kill")
    
    print("Step 2: Starting monitor mode on wlan0...")
    run_command("sudo airmon-ng start wlan0")

def stop_monitor():
    print("Step 5: Stopping monitor mode...")
    run_command("sudo airmon-ng stop wlan0")
