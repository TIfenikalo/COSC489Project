#This implements the rockyou file to crack passwords
from utils import run_command

def crack_password(filename):
    print("Step 6: Cracking password with aircrack-ng and rockyou.txt...")
    cap_file = f"{filename}-01.cap"
    run_command(f"sudo aircrack-ng {cap_file} -w /usr/share/wordlists/rockyou.txt")
