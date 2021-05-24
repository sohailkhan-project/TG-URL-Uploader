import os

class Config(object):

    # get a token from https://chatbase.com

    CHAT_BASE_TOKEN = "9d33fd59-c984-4934-900e-b405136cf4fc"

    # get a token from @BotFather

    TG_BOT_TOKEN = "1388215116:AAFSHhhYtLFwpmp1vD74R81C-TdK_y_Cs-w"

    # The Telegram API things

    APP_ID = 1089218

    API_HASH = "b6bdbb931516e5f9405f96ae129a412a"

    # Get these values from my.telegram.org

    # Array to store users who are authorized to use the bot

    AUTH_USERS = 1230663194

    # Banned Unwanted Members..



# the download location, where the HTTP Server runs

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    # Update channel for Force Subscribe

    UPDATE_CHANNEL = 1001206840005

    # Telegram maximum file upload size

    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000

    # chunk size that should be used with requests

    CHUNK_SIZE = 128

    # default thumbnail to be used in the videos

    DEF_THUMB_NAIL_VID_S = "https://placehold.it/90x90"

    # proxy for accessing youtube-dl in GeoRestricted Areas

    # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061

    HTTP_PROXY = 36.255.211.1:54623

    # https://t.me/hevcbay/951

    OUO_IO_API_KEY = ""

    # maximum message length in Telegram

    MAX_MESSAGE_LENGTH = 4096

    # set timeout for subprocess

    PROCESS_MAX_TIMEOUT = 3600

    # watermark file

    DEF_WATER_MARK_FILE = ""
