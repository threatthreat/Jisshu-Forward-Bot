# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "16708960")
    API_HASH = environ.get("API_HASH", "dda7630be99593256cb7c520eae0ce6d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7925662961:AAGSN-pYYRHypKjb-qfm8CFc-ri5caQOwaA") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '5482962500').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Tylerdurden:tyler1234@cluster0.ptqpxti.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002650191240'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "False")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
