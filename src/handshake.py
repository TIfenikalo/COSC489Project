def capture_handshake(bssid, channel, filename):
    print("Step 4: Capturing handshake. Press CTRL+C when handshake is captured.")
    command = f"sudo airodump-ng -w {filename} -c {channel} --bssid {bssid} wlan0mon"
    run_command(command)
