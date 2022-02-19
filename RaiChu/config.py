## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
API_ID = int(getenv("API_ID", "18319188"))
API_HASH = getenv("API_HASH", "d2e8e7c8d8aa4bf118d3205bef40a137")
OWNER_NAME = getenv("OWNER_NAME", "darmandj")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "ribaajosmani")
BOT_USERNAME = getenv("BOT_USERNAME", "Osmani_Player_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "osmanigroupbot")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "osmanibots")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/1cbf94f1df06596632c7b.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/levina-lab/video-stream")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/65a1b60c52c56e3ea2bf4.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/047144efdfe99077eb857.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/0bef4d232d9ce7d1c6223.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/047144efdfe99077eb857.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/aba2871fb1eb63fdd7c94.jpg")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/faef9b52220b3d09eb14f.png")
