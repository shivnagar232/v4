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
BOT_TOKEN = "6508501033:AAHIFTa3Xbkx5NjcQPBnukt_KxdmSXfwHs4" #config("BOT_TOKEN", default=None)
SESSION = "BQGTAMIAYFP0yfcy0sII4sAzyK5JjbGgFiMb6gVHy44_z4mACuzU6Gl8MGMl5h_89_Rt5kwcCskrNkRlQKA6NeS1R7FNzLy21QSKNxqTblzdwdyQGVNId15YnhH4ZZAGZiiJ69M0h6SRwac_b3m9nOHQnReXi0wdJ8tEG9CYc7kHXMLzQD8DrJh_RmJOnMwl0fSe_8FAxB4abVImyAHOOyZoqjrzeuPD-sSkUotycQ2IqXie6tyiNBypAmSfniAIkVGZXj500fJvb30X7_04C3IMYijpCzx22Mf_npl-xLavYBgOszFRT8SeQ6o6mBcR3svC-u3MMIvxE2JOmq59IskX9ZBDIgAAAAAiRSpcAA" #config("SESSION", default=None)
FORCESUB = "dev_gagan" #config("FORCESUB", default=None)
AUTH = "574958172" #config("AUTH", default=None))
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
