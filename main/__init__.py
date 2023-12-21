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
BOT_TOKEN = "6772931491:AAE57eXG48TT0NfqQhc8YYKFn25gdjq8Oxk" #config("BOT_TOKEN", default=None)
SESSION = "BQGTAMIAET-dFCit0hh9TPIW8A1NIKlwmZzy6aytxsXD8D9jDZAWZa9xZsnQh3UHs93GVrUPFBDEbXqy_x2rSgHcRLhIUboUkvMAf_600f2MbAK-KShLpyb94JMzQvldp_9fhqCb9huU8L7Nxt7II4Wg7E2OujtNEqTDOyO9DmbIn4AAJK9zG1Tts0rwlAKEPrBAIbZ-mENExVGv-Q67_etGS4DeH7f5DowowqefGUbljnT34LvEXjSlThLONe3rLv55C7M6-pQh_y5_uhyzuUc4UbmrNYbnPZrIlHiNIC8lfdzeq9NwWhwozWEU_u5zORqxhBevoqsMeI394Ns6DWBx3Cx0xgAAAAFpF4RKAA" #config("SESSION", default=None)
FORCESUB = "dev_gagan" #config("FORCESUB", default=None)
AUTH = "6518701261" #config("AUTH", default=None))
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
