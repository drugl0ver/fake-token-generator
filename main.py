import os
import time
import ctypes
import base64
import random
import secrets
import requests
import threading
import charlogger
from colorama import Fore
from pystyle import Cursor

logger = charlogger.Logger(
    default_prefix="<TIME> | token gen"
)


def cls():
    os.system("cls" if os.name == "nt" else "clear")


global unlocked, locked
unlocked = 0
locked = 0


def setStats():
    ctypes.windll.kernel32.SetConsoleTitleW(f"Token Gen ; unlocked: {unlocked} , locked: {locked}")


def menu():
    Cursor.HideCursor()
    cls()
    setStats()
    banner = requests.get("https://pastebin.com/raw/5w6bswQy").text
    print(f"\n\n{Fore.MAGENTA}{banner}")
    logger.info(title="STARTED", data="GENERATOR")
    threads = [threading.Thread(target=generate) for i in range(50)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


def getRandomTokens():
    user_id = (base64.b64encode(f"110688481879865{random.randint(1000, 9999)}".encode("ascii")).decode("ascii")).replace("==", "")
    middle = f"{secrets.token_urlsafe(6)}"
    end = f"{secrets.token_urlsafe(6)}_{secrets.token_urlsafe(31)}"
    return f"{user_id}.{middle}.{end[:-16]}[...]"


def generate():
    global locked, unlocked
    token = getRandomTokens()
    time.sleep(random.uniform(2.5, 5.5))
    locker = random.randint(1, 100)
    if locker < 12:
        logger.warn(title="LOCKED", data=f"{' '*9}{token}")
        locked += 1
        setStats()
        return None
    else:
        unlocked += 1
        setStats()
        logger.info(title="UNLOCKED", data=f"{' '*7}{token}")
    time.sleep(random.uniform(5.5, 7.2))
    logger.info(title="EMAIL VERIFIED", data=f' {token}')
    time.sleep(random.uniform(7.5, 10.5))
    logger.info(title="PHONE VERIFIED", data=f' {token}')
    threading.Thread(target=generate).start()


menu()
