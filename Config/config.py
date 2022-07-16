import logging
import os
import sys
import time
import spamwatch
import aiohttp

import telegram.ext as tg
from redis import StrictRedis
from Python_ARQ import ARQ
from pyrogram import Client, errors
from telethon.sessions import StringSession
from telethon import TelegramClient
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


    INFOPIC = int(getenv('INFOPIC', "true"))
    EVENT_LOGS = getenv('EVENT_LOGS', "-100")
    WEBHOOK = int(getenv('WEBHOOK', "False"))
    ARQ_API_URL = getenv("ARQ_API_URL", "https://thearq.tech/")
    ARQ_API_KEY = getenv("ARQ_API_KEY", "")
    URL = getenv('URL', "")  # Does not contain token
    PORT = int(getenv('PORT', 5000))
    CERT_PATH = getenv("CERT_PATH")
    API_ID = getenv('API_ID', "")
    API_HASH = getenv('API_HASH', "")
    DB_URI = getenv('DATABASE_URL', "")
    DONATION_LINK = getenv('DONATION_LINK', "")
    LOAD = getenv("LOAD", "").split()
    NO_LOAD = getenv("NO_LOAD", "rss").split()
    DEL_CMDS = int(getenv('DEL_CMDS', "true"))
    STRICT_GBAN = int(getenv('STRICT_GBAN', "true"))
    WORKERS = int(getenv('WORKERS', "8"))
    BAN_STICKER = getenv('BAN_STICKER',
                                 'CAADAgADOwADPPEcAXkko5EB3YGYAg')
    ALLOW_EXCL = getenv('ALLOW_EXCL', "true")
    CASH_API_KEY = getenv('CASH_API_KEY', "-xyz")
    TIME_API_KEY = getenv('TIME_API_KEY', "-xyz")
    AI_API_KEY = getenv('AI_API_KEY', "")
    WALL_API = getenv('WALL_API', "")
    SUPPORT_CHAT = getenv('SUPPORT_CHAT', "https://t.me/AkenoSupport00")
    SPAMWATCH_SUPPORT_CHAT = getenv('SPAMWATCH_SUPPORT_CHAT', "")
    SPAMWATCH_API = getenv('SPAMWATCH_API', " ")
    REPOSITORY = getenv("REPOSITORY", "https://github.com/Subhradeep00/Akenobot")
    IBM_WATSON_CRED_URL = getenv("IBM_WATSON_CRED_URL", "")
    IBM_WATSON_CRED_PASSWORD = getenv("IBM_WATSON_CRED_PASSWORD", "")
    TEMP_DOWNLOAD_DIRECTORY = getenv("TEMP_DOWNLOAD_DIRECTORY", "./")
    HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")
    TELEGRAPH_SHORT_NAME = getenv("TELEGRAPH_SHORT_NAME", "Akatsuki")
    HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
    BOT_NAME = getenv("BOT_NAME", "Akeno") # Name Of your Bot.4
    BOT_USERNAME = getenv("BOT_USERNAME", "Akeno00bot") # Bot Username
    OPENWEATHERMAP_ID = getenv("OPENWEATHERMAP_ID", "") # From:- https://openweathermap.org/api
    LOG_GROUP_ID = getenv('LOG_GROUP_ID', "-100")
    BOT_ID = getenv("BOT_ID", "")
    ERROR_LOGS = getenv("ERROR_LOGS", "-100") # Error Logs (Channel Ya Group Choice Is Yours) (-100)
    STRICT_GMUTE = int(getenv('STRICT_GMUTE', "True"))
    MONGO_DB_URI = getenv("MONGO_DB_URI", "")
    DEBUG = int(getenv('IS_DEBUG', "False"))
    REDIS_URL = getenv("REDIS_URL", "") # REDIS URL (From:- Heraku & Redis)
    OWNER_NAME = getenv("OWNER_NAME", "")
