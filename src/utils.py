import subprocess

def run_command(command):
    """Run a command in terminal and stream output."""
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Command failed: {command}")
