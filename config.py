from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "43e998f17bcf1f69f85b6d4022dffde2")
      API_ID = int(getenv("API_ID", "29224205"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7485782184:AAEXhTDcKsXSpxrPE0SJTRnAozOt0uHFpWw")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-2168553128:-2237536374", " ").split(' '))


# Don't Remove Credit @Hacker_ks
# Subscribe YouTube Channel For Amazing Bot @Hacker_ks
# Ask Doubt on telegram @Hacker_ks
