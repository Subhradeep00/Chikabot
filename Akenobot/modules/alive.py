import asyncio
import telegram
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from Akenobot.events import register
from Akenobot import telethn as borg, OWNER_ID, OWNER_NAME
from Akenobot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins
from pyrogram import __version__ as pyro


edit_time = 5
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/333f0bb89a2792553bd9a.jpg"
file2 = "https://telegra.ph/file/333f0bb89a2792553bd9a.jpg"
file3 = "https://telegra.ph/file/333f0bb89a2792553bd9a.jpg"
file4 = "https://telegra.ph/file/333f0bb89a2792553bd9a.jpg"
""" =======================CONSTANTS====================== """

START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    Akeno = f"➛ 「 ʜᴇʏ [{yes.sender.first_name}](tg://user?id={yes.sender.id}), I'm 𝒜𝓀ℯ𝓃ℴ 」\n"
    
    Akeno += f"➛ 「 ᴜᴘᴛɪᴍᴇ 」 ~ `{uptime}`\n"
    
    Akeno += f"➛ 「 ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ 」 ~ `{version.__version__}`\n"
    
    Akeno += f"➛ 「 ᴘᴛʙ ᴠᴇʀsɪᴏɴ 」 ~ `{telegram.__version__}`\n"
    
    Akeno += f"➛ 「 ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ 」 ~ `{pyro}`\n"
    
    Akeno += f"➛ 「 ᴍʏ ᴍᴀsᴛᴇʀ 」 ~ [ᴀᴋᴀᴛsᴜᴋɪ](tg://user?id={OWNER_ID})\n\n"
    
    Akeno += f"ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ɪɴ {yes.chat.title}"
    BUTTON = [[Button.url("sᴜᴘᴘᴏʀᴛ", "https://t.me/AkenoSupport00"), Button.url("ᴜᴘᴅᴀᴛᴇs", "https://t.me/AkenoSupport0")]]
    on = await borg.send_file(yes.chat_id, file="https://te.legra.ph/file/ce84881970d9514a62fd4.jpg",caption=Akeno, buttons=BUTTON)

@register(pattern=("/repo"))
async def repo(yes):
    Akeno = f"**Hey [{event.sender.first_name}](tg://user?id={event.sender.id}), Click The Button Below To Get My Repo**\n\n"
    BUTTON = [[Button.url("GitHub", "https://github.com/Subhradeep00/Akenobot"), Button.url("Developer", "https://t.me/Subhradeep00")]]
    await borg.send_file(event.chat_id, file="https://te.legra.ph/file/ce84881970d9514a62fd4.jpg", caption=Akeno, buttons=BUTTON)
