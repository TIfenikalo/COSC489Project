# Wi-Fi Security Auditing Tool

## Overview
This tool captures WPA/WPA2 handshakes and attempts password cracking using Aircrack-ng. **Use ethically and legally.**
Wi-Fi Security Auditing Tool
A Ethhical Hacking Project
Contributors: Antonio Jackson, Titorian Huggins, Tobiloba Ifenikalo

## Features
- Enable monitor mode
- Scan and select Wi-Fi networks
- Capture WPA/WPA2 handshakes
- Perform optional deauthentication
- Crack handshake using rockyou.txt wordlist

## System Requirements
-OS: Kali Linux (or Debian-based Linux)
-Python 3.x
-Wireless Adapter that supports monitor mode and packet injection (e.g., Alfa AWUS036ACH)
-Wordlist: rockyou.txt (found at /usr/share/wordlists/ on Kali)

## Setup Instructions
1. git clone https://github.com/TIfenikalo/COSC489Project.git
cd COSC489Project
2. pip install -r requirements.txt
3. sudo apt update
sudo apt install aircrack-ng




Folder Structure
COSC489Project/
├── docs/
│   └── ethical-guidelines.md
├── src/
│   └── main.py
├── tests/
│   └── test_dummy.py
├── .gitignore
├── README.md
└── requirements.txt

Ethical Considerations
Do NOT test on networks you don’t own or have explicit permission to test.

This tool is for educational and ethical hacking purposes only.


