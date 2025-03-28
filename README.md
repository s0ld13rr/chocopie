# chocopie - Red Team Host Reconnaissance Tool 🥧

## Description
This tool is designed for reconnaissance on a host system, specifically to check for the presence of VPN configuration files. It scans the system drive (`C:\`) for OpenVPN configuration files (`.ovpn`) and extracts VPN-related configurations from CheckPoint Endpoint Connect logs. The found data is then automatically sent to a Telegram bot.

## Features
- Scans `C:\Users\` for `.ovpn` files.
- Extracts VPN-related configurations from CheckPoint's `trac.log`.
- Sends collected configurations to a specified Telegram chat.
- Deletes files after processing to remove traces.

## Requirements
- Python 3.8+
- Required Python modules:
  - `aiogram`
  - `asyncio`
  - `os`


## Installation
1. Clone the repository or download the script.
2. Install dependencies:
   ```bash
   pip install aiogram
   ```
3. Create a Telegram bot using [BotFather](https://t.me/BotFather) and obtain the bot token.
4. Set up the required variables in the script:
   ```python
   TOKEN = "your_bot_token_here"
   CHAT_ID = 123123123 # your tg chat id, must be int
   ```

## Usage
Run the script:
```bash
python chocopie.py
```
Or you may compile it with PyInstaller:
```bash
chocopie.exe
```
![POC](https://github.com/s0ld13rr/chocopie/blob/main/PoC.jpg)

The script will:
1. Search for `.ovpn` files on the `C:\` drive.
2. Extract VPN configuration details from CheckPoint's logs.
3. Send the findings to the configured Telegram chat.
4. Optionally, delete the extracted files after sending.

## Disclaimer
This tool is for educational and research purposes only. Unauthorized use on systems you do not own is illegal.

