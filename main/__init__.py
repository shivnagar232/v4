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
BOT_TOKEN = "6582884232:AAG6gEZceA6F2giuD7WtaZVOswLnaXtuHtE" #config("BOT_TOKEN", default=None)
SESSION = "BQFQdkwABI6dHGiDHYL610Q11Bw53J_4aVI-T8Gcqtk_cacD9foBPgo-yclHDBAVOSwcM95pTgdw_G7DJv3uIbO9WDc4Ar5vy-JqseXEUQ89WjGeRRbhxN75JCSKK6NJbVrkgaBvNqEChMRPMc10jb6QUwUtq_zePPgz13upF2axr5NoV07zs3S7fr4fUJixH5cuVRQw2qxxeuDTGhWTOOCr2AYaM6bGmU9Jq51asc4oW7j_KDo06Z0jMep_c4gIT2rykKMVK6iLzJ11NQkDdwdBMTNH5eCQ0-4f_Qn8vcZWqWwNktybPAu-H3_i1JQFAvbv1b5mzio2u2tLTLabCkTgVDeseQAAAAGYVIviAA" #config("SESSION", default=None)
FORCESUB = "dev_gagan" #config("FORCESUB", default=None)
AUTH = "1874469918" #config("AUTH", default=None))
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
