import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/3da6660d23fc47c434f82.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"** [{event.sender.first_name}](tg://user?id={event.sender.id}) I'm MADARA Uchihað´.** \n\n"
  TEXT += "ð´ **ðð¨ ð§ð¨ð­ ð¦ð¢ð¬ð®ð§ððð«ð¬ð­ðð§ð ð­ð¡ð¢ð¬, ð­ð¡ð¢ð¬ ð¢ð¬ ð§ð¨ð­ ð²ð¨ð®ð« ð©ð¨ð°ðð« ð¨ð ðð«ððð­ð¢ð¨ð§** \n\n"
  TEXT += f"ð´ **My Lord : [Your Dad](https://t.me/Lord_DSP_3)** \n\n"
  TEXT += f"ðï¸ **Library Version :** `{telever}` \n\n"
  TEXT += f"ðï¸ **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"ðï¸ **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**I'm back alive and Reanimate agian to this cursed world, hmm...**"
  BUTTON = [[Button.url("Help", "https://t.me/Uchiha_Madara_Robot?start=help"), Button.url("Support", "https://t.me/Anime_Gaming_chat_global")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
