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
BOT_TOKEN = "6707898403:AAHJWvJ1aHxJZgWzpZpuDSMs0VfebSrfLFs" #config("BOT_TOKEN", default=None)
SESSION = "BQGTAMIAXQtr5-koY6BTlj8JejI0dGPGtUh-uwcqud5Lk-cY4Rlly9FXC4QxjXUpeorGqc2cih1N9pcOWduW0us1M4NmH-bu61tt5SFu_s5xbl_iO242yJsZPuIyrqnQLJM8wvGy1OuvEbO332F32awAlkLvik4FKpuqBIeyYEIQ_CYYIa7NpEWpBwy4w5fqe7ihbnlS_zXjhhvG05l7mEabLlqVzNykSQnzeFZ-OqQP8TY5qbqZRR3bto_G06KoK4-nDFQNrWt9fMaFsF1Gnpi1CRgqVBlsVGqXjLbdZQrb5790AQl9KQtHjIfv_g_hDylVGfOf_wax81uJdSF6bbiTEVQe_QAAAAGQ_sIBAA" #config("SESSION", default=None)
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
