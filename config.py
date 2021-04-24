import os

class Config(object):
    # get a token from https://chatbase.com
    CHAT_BASE_TOKEN = "71e297e0-81ea-4f71-9d67-ec46f90e0b85"
    # get a token from @BotFather
    TG_BOT_TOKEN = "1627208503:AAGKtYcTP3Uyll_RwZ2dGSquDGSLLVj97RU"
    # The Telegram API things
    APP_ID = 1089218
    API_HASH = "b6bdbb931516e5f9405f96ae129a412a"
    # Get these values from my.telegram.org
    # Array to store users who are authorized to use the bot
    AUTH_USERS = 1230663194
    # the download location, where the HTTP Server runs
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    # Update channel for Force Subscribe
    UPDATE_CHANNEL = "TechWithLoot"
    # Telegram maximum file upload size
    MAX_FILE_SIZE = 50000000
    TG_MAX_FILE_SIZE = 2097152000
    FREE_USER_MAX_FILE_SIZE = 50000000
    # chunk size that should be used with requests
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    # default thumbnail to be used in the videos
    DEF_THUMB_NAIL_VID_S = "https://telegra.ph/file/3c1be012bf847347f97e7.jpg"
    # proxy for accessing youtube-dl in GeoRestricted Areas
    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    # https://t.me/hevcbay/951
  
    MAX_MESSAGE_LENGTH = 4096
    # set timeout for subprocess
    PROCESS_MAX_TIMEOUT = 3600
    # watermark file
    DEF_WATER_MARK_FILE = "https://telegra.ph/file/3c1be012bf847347f97e7.jpg"
