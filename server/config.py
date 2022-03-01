class Config(object):
    TOKEN = '' # 봇 토큰
    OWNERS = [] # 관리자의 아이디
    commandInt = "." # 명령인자

class Production(Config):
    LOGGER = False

class Development(Config):
    LOGGER = True