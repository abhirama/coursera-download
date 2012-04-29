import cookielib, urllib2, urllib, ConfigParser, pprint

class Config(object): 
    SECTION_CREDENTIALS = 'credentials'
    SECTION_CREDENTIALS_USERNAME = 'username'
    SECTION_CREDENTIALS_PASSWORD = 'password'

    SECTION_DOWNLOAD = 'download'
    SECTION_DOWNLOAD_CLASS = 'class'

    CONFIG_FILE = 'download.cfg'

    LOGIN_URL = 'https://www.coursera.org/maestro/auth/api/user/login'
    REDIRECT_URL = 'https://class.coursera.org/{0}/auth/auth_redirector?type=login&subtype=normal&email=&visiting=%2F{0}%2Flecture%2Findex&minimal=true'

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(Config.CONFIG_FILE)
        self.username = config.get(Config.SECTION_CREDENTIALS, Config.SECTION_CREDENTIALS_USERNAME)
        self.password = config.get(Config.SECTION_CREDENTIALS, Config.SECTION_CREDENTIALS_PASSWORD)
        self.course = config.get(Config.SECTION_DOWNLOAD, Config.SECTION_DOWNLOAD_CLASS)
        self.clazz = self.getJustClass(self.course)
        self.loginURL = Config.LOGIN_URL
        self.redirectURL = Config.REDIRECT_URL.format(self.clazz)

    def getJustClass(self, courseURL):
        splits = courseURL.split('/')
        return splits[3]

def getVideoPage(config):
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

    formParams = {
        'email_address': config.username,
        'password': config.password,
    }

    formParams = urllib.urlencode(formParams)

    print config.loginURL
    opener.open(config.loginURL, formParams)
    print config.redirectURL
    opener.open(config.redirectURL)
    r = opener.open(config.course)

    return r.read()

config = Config()
print getVideoPage(config)
#getJustClass(config)
