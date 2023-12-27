#Github.com/mrinvisible7

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("telethon").setLevel(logging.WARNING)


# variables
API_ID = "26075120" #config("API_ID", default=None, cast=int)
API_HASH = "1fda88a5d1de46058a4791c78bce198e" #config("API_HASH", default=None)
BOT_TOKEN = "6349487980:AAE_PvThCH5WHp1y7y7bJThQdzmAG-BNs8g" #config("BOT_TOKEN", default=None)
SESSION = "BQGTAMIAQmZfN-UwPli-poSBAJ0YEBzM-ziBw0YbP0oC3GaL6YIC-kcCEY9S3KH_mwnRLRCqNelP8LNM4uKBdjj3tP13yoo5JCzS9H63sWH8jfG0OnqtJRxBkhFCDLnrm64jh13F9JT9NL0Bi5-DQJUaFl2BuO1LXhUGVVr_ZtZddwQ-qj7mtCzp0OEr29D7NF-RD1AOZB8N37brRxiZFh5X4HU4eHM_1GKhNmL1qS5E7A4dUpgrJvyZuoxKV8eEnDdwj6Txs-Illn_Sz8W8iXewCt-xSZI_I5fv6KhB7v6MWTvlk7OSjlGw5F4uH7_Gsk3Y9qs73pQUhRVNqQjOATVMm97HMwAAAABCYOXEAA" #config("SESSION", default=None)
FORCESUB = "dev_gagan" #config("FORCESUB", default=None)
AUTH = "1113646532" #config("AUTH", default=None))
SUDO_USERS = []
if len(AUTH) != 0:
    SUDO_USERS = {int(AUTH.strip()) for AUTH in AUTH.split()}
else:
    SUDO_USERS = set()

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

#userbot = Client(
#    session_name=SESSION, 
#    api_hash=API_HASH, 
#    api_id=API_ID)
userbot = Client("myacc",api_id=API_ID,api_hash=API_HASH,session_string=SESSION)

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    #print(e)
    logger.info(e)
    sys.exit(1)
