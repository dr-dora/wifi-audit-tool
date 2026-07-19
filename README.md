# WiFi Audit Tool

A Bash + Python utility that automates Wi-Fi network discovery and packet capture for authorized wireless security assessments.

> ⚠️ This project is intended for educational purposes and for testing wireless networks that you own or have explicit permission to assess.

---

## Features

- Scan nearby Wi-Fi networks
- Parse `airodump-ng` CSV output automatically
- Interactive network selection
- Enable monitor mode
- Capture WPA/WPA2 authentication traffic
- Automate the Aircrack-ng workflow

---

## Technologies

- Bash
- Python 3
- Aircrack-ng Suite
- Linux
- Wireless networking

---

## Project Structure

```
.
├── script.sh          # Main automation script
└── select_wifi.py     # Parses CSV scan results and allows network selection
```

---

## Requirements

- Linux
- Python 3
- Aircrack-ng Suite
- Wireless adapter supporting Monitor Mode

---

## Usage

Clone the repository:

```bash
git clone https://github.com/dr-dora/wifi-audit-tool.git
```

Run the script:

```bash
chmod +x script.sh
sudo ./script.sh
```

The program will:

1. Enable Monitor Mode
2. Scan nearby Wi-Fi networks
3. Display detected networks
4. Allow selecting a target network
5. Start packet capture

---

## Future Improvements

- Better terminal UI
- Automatic handshake verification
- Logging
- Support for multiple wireless interfaces
- Configuration file
- Error handling improvements

---

## Disclaimer

This software is provided for educational and defensive security purposes only.

The author is not responsible for any misuse of this software.

Use only on networks that you own or have explicit permission to test.

---

## Author

**dr-dora**

GitHub: https://github.com/dr-dora
