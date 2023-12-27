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
SESSION = "BQGTAMIAqE3F9Qf5BGrdby7ZgPqNHST57Gxt232JrgPVbIqkfI9KabcIOgbBlDdvFVmf6ZP7UJbIDNjxG5aXFPgKEfSOlAkVQqGlBa0qOHBdNV_wPmiIog0ecHFR6QSnjQgl7UQSpvOcDFSn-rDaDqIcbRaArNOC_hh4jX81I92SGXQQdeGSIBg-b8wpsbY9lHWPfldpkasMAccMgN43vYC20P_DwolOSI6sOLE6qnEg0WVfDgC7Z-MJOU-iCY6Baul2dz4RXjCVJ_OIdTCSwXfJpZpm7mrg2oKg3gWfqiUwcaaJ38oQsKqDQ0pnBuH6hrjNaXSfONUWhjZxY9QT3mCYTBreuQAAAABCYOXEAA" #config("SESSION", default=None)
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
