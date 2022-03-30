
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from RaiChu.config import BOT_NAME as bn
from Process.filters import other_filters2
from time import time
from datetime import datetime
from Process.decorators import authorized_users_only
from RaiChu.config import BOT_USERNAME, ASSISTANT_USERNAME

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("Asbuuc", 60 * 60 * 24 * 7),
    ("Malinta", 60 ** 2 * 24),
    ("Saca", 60 ** 2),
    ("Daqiiqada", 60),
    ("Mirirka", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@Client.on_message(other_filters2)
async def start(_, message: Message):
        await message.reply_text(
        f"""**👋Salama'Aniga Waxaan Ahay 𝙊𝙨𝙢𝙖𝙣𝙞 𝘽𝙤𝙩 Botkaan 
        Waxa aad gashan kartaa Oo ku isticmaali kartaa Group kaaga.
        [Maamulaha](https://t.me/Seyriye) Thanks to add me 😇**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "😎ᴏᴡɴᴇʀ😎", url="https://t.me/ribajosmani"
                    ),
                    InlineKeyboardButton(
                        "ᴄᴏᴍᴍᴀɴᴅ🦍", url="https://telegra.ph/%F0%9D%99%8A%F0%9D%99%A8%F0%9D%99%A2%F0%9D%99%96%F0%9D%99%A3%F0%9D%99%9E-%F0%9D%98%BD%F0%9D%99%A4%F0%9D%99%A9-02-19"
                    )
                  ],[
                    InlineKeyboardButton(
                       " 🇸🇴sᴜᴘᴘᴏʀᴛ", url="https://t.me/osmanigroupbot"
                    ),
                    InlineKeyboardButton(
                        "ᴜᴘᴅᴀᴛᴇ📢", url="https://t.me/teamosmani"
                    )
                ],[
                    InlineKeyboardButton(
                        "➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                        url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )
