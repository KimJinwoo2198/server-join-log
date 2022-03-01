import os
import sys
import logging
ENV = bool(os.environ.get('ENV', False))

if ENV:
    TOKEN            = os.environ.get('TOKEN', None)
    commandInt       = os.environ.get('commandInt', "/")

else:
    from server.config import Development as Config

    TOKEN            = Config.TOKEN
    commandInt       = Config.commandInt

EXTENSIONS = list(EXTENSIONS)

BOT_NAME_TAG_VER = "%s%s" %(BOT_NAME, BOT_TAG)
