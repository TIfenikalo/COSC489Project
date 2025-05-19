import subprocess # Used to run terminal commands in python

def capture_handshake(interface, bssid, channel, output_prefix):
    subprocess.run(['airodump-ng', '--bssid', bssid, '-c', channel, '-w', output_prefix, interface])

