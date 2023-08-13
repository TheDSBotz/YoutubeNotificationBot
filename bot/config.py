#    This file is part of the Youtube Notification  distribution.
#    Copyright (c) 2022 kaif_00z
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, version 3.
#
#    This program is distributed in the hope that it will be useful, but
#    WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
#    General Public License for more details.
#
# License can be found in <
# https://github.com/kaif-00z/YoutubeNotificationBot/blob/main/License> .


from decouple import config

try:
    APP_ID = 10956858
    API_HASH = config("API_HASH", default="cceefd3382b44d4d85be2d83201102b7")
    BOT_TOKEN = "5831494259:AAFhCj-c0y-s532guoKBJQUXVdEeDUOnfD"
    YT_API_KEY = "AIzaSyD2OxLGCesQEiF1qo8D9tVlUtlroeWKlPo"
    OWNER = 1125671241
    CHAT = 1125671241
    CH_ID = "SonySAB"
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit()
