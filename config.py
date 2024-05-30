from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "43e998f17bcf1f69f85b6d4022dffde2")
      API_ID = int(getenv("API_ID", "29224205"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "7485782184:AAEXhTDcKsXSpxrPE0SJTRnAozOt0uHFpWw")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001722984461:-1001623633000").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
