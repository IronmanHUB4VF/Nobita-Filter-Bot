import re, logging
from os import environ
from Script import script
from dotenv import load_dotenv
load_dotenv()


id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ.get('API_ID', '24736263'))
API_HASH = environ.get('API_HASH', '4d53732917b73a6bb89c3b2f2f7b0902')
BOT_TOKEN = environ.get('BOT_TOKEN', '5885485749:AAEjcZgZHEt2KV3j9oEm71S-LvPcEezA9Hc')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/9354a124921994bf84d86.jpg https://telegra.ph/file/8233d87aedf440497a428.jpg https://telegra.ph/file/b4ba8852086d311226e1d.jpg https://telegra.ph/file/55c8dbfa80cf494a2af50.jpg https://telegra.ph/file/a5ecb192e1a0cae82412a.jpg https://telegra.ph/file/e3c85682af8c575a78b5d.jpg https://telegra.ph/file/0355bd3a158f22171f2d5.jpg https://telegra.ph/file/b64a61bbe2245c5ca6141.jpg https://telegra.ph/file/c545eaea593e14d256b25.jpg https://telegra.ph/file/a883451badabf41bb5fe8.jpg https://telegra.ph/file/4e2f727e0055e47c19b9e.jpg https://telegra.ph/file/52fbb1e7864a571e7fa23.jpg https://telegra.ph/file/4147c2a1086e6041c31cb.jpg https://telegra.ph/file/72f563d7c4bedf1b2221c.jpg https://telegra.ph/file/a235ea8103a073c3879cf.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/61ef9818986cef9554017.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/61ef9818986cef9554017.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/61ef9818986cef9554017.jpg")

# Admins, Channels & User
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1228255863 5257925921').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1001878326006 -1001895151847').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_grp = environ.get('AUTH_GROUP', '')
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('SUPPORT_CHAT_ID', '-1001729944512')
reqst_channel = environ.get('REQST_CHANNEL_ID', '-1001968931458')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

#Downloader
DOWNLOAD_LOCATION = environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS/AudioBoT/")

# This is required for the plugins involving the file system.
TMP_DOWNLOAD_DIRECTORY = environ.get("TMP_DOWNLOAD_DIRECTORY", "./DOWNLOADS/")

# Open AI
OPENAI_API = environ.get('OPENAI_API', '0')
if len(OPENAI_API) == 0:
    logging.warning('OPENAI_API is empty')
    exit()

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://Lazyiron:bhargavp1937@cluster7.31obcsb.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster7")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Iron_file')

# stickers
STICKERS = (environ.get('STICKERS', 'CAACAgUAAxkBAAIKqWP81BZ6YnpWEFoF_4JPR0EbjsO3AAIvBwACnMjpV9YvaONl41IBHgQ CAACAgUAAxkBAAIKrmP81GnWQ0d_BAZhre0dMc5SwJKOAAJ0DgACgr3gVwrjYuxSJxn7HgQ')).split()

# FSUB
auth_channel = environ.get('AUTH_CHANNEL', '-1001685314725')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
# Set to False inside the bracket if you don't want to use Request Channel else set it to Channel ID
REQ_CHANNEL = environ.get("REQ_CHANNEL", "-1001586793024")
REQ_CHANNEL = int(REQ_CHANNEL) if REQ_CHANNEL and id_pattern.search(REQ_CHANNEL) else False
JOIN_REQS_DB = environ.get("JOIN_REQS_DB", DATABASE_URI)

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '-1001506017287').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
IS_VERIFY = bool(environ.get('IS_VERIFY', False))
VERIFY2_URL = environ.get('VERIFY2_URL', "omegalinks.in")
VERIFY2_API = environ.get('VERIFY2_API', "1c68341ce1ff1858a7e82f00812898da69d44a0c")
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'omegalinks.in')
SHORTLINK_API = environ.get('SHORTLINK_API', '1c68341ce1ff1858a7e82f00812898da69d44a0c')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', False))
NO_RESULTS_MSG = bool(environ.get('NO_RESULTS_MSG', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
S_GROUP = environ.get('S_GROUP',"https://t.me/movie_and_series_hub4vf") #suppot group full link
RUL_LNK = environ.get('RUL_LNK',"https://graph.org/%F0%9D%97%A0%F0%9D%9E%93%F0%9D%97%A6%F0%9D%97%A7%F0%9D%9E%9D%F0%9D%97%A5-02-15")
MAIN_CHANNEL = environ.get('MAIN_CHANNEL',"https://telegram.me/HUB4VF") #main channel full link
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/+q2AEU8SWC1Q2NmJl') # movie or series full link
CHNL_LNK = environ.get('CHNL_LNK', 'https://telegram.me/HUB4VF') # if you have any movie series channel then full link else main channel link
OWN_LNK = environ.get('OWN_LNK',"https://telegram.me/LazyIron") # owner or admin user full link if you want to put else you can put support group link or contact bot link
MVG_LNK = environ.get('MVG_LNK',"https://t.me/+q2AEU8SWC1Q2NmJl") # movie group full link
MSG_ALRT = environ.get('MSG_ALRT', 'ꜱʜᴀʀᴇ  ᴀɴᴅ  ꜱᴜᴘᴘᴏʀᴛ  ᴜꜱ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1001862601820'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'movie_and_series_hub4vf') #support group username without fill link or @
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1001878326006')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), False)

LANGUAGES = ["hindi", "hin", "tamil", "tam", "telugu", "tel", "english", "eng", "kannada", "kan", "malayalam", "mal"]
TUTORIAL = environ.get('TUTORIAL', 'https://youtu.be/rddlpYLm0G0')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', False))

# Online Stream and Download
NO_PORT = bool(environ.get('NO_PORT', False))
APP_NAME = None
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = environ.get('APP_NAME')
else:
    ON_HEROKU = False
BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else \
    "https://{}/".format(FQDN, PORT)
SLEEP_THRESHOLD = int(environ.get('SLEEP_THRESHOLD', '60'))
WORKERS = int(environ.get('WORKERS', '4'))
SESSION_NAME = str(environ.get('SESSION_NAME', 'LazyBot'))
MULTI_CLIENT = False
name = str(environ.get('name', 'LazyPrincess'))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if 'DYNO' in environ:
    ON_HEROKU = True
    APP_NAME = str(getenv('APP_NAME'))

else:
    ON_HEROKU = False
HAS_SSL=bool(getenv('HAS_SSL',False))
if HAS_SSL:
    URL = "https://{}/".format(FQDN)
else:
    URL = "https://{}/".format(FQDN)



LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
