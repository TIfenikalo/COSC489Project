# Wi-Fi Security Auditing Tool

## Overview
This tool captures WPA/WPA2 handshakes and attempts password cracking using Aircrack-ng. **Use ethically and legally.**

## Features
- Enable monitor mode
- Scan and select Wi-Fi networks
- Capture WPA/WPA2 handshakes
- Perform optional deauthentication
- Crack handshake using rockyou.txt wordlist

## Setup Instructions
1. Install dependencies:
   ```bash
   sudo apt install aircrack-ng
   pip install -r requirements.txt

2. Run the tool
   python3 src/main.py

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


