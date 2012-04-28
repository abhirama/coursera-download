import cookielib, urllib2, urllib, ConfigParser

class Config(object): 
    SECTION_CREDENTIALS = 'credentials'
    SECTION_CREDENTIALS_USERNAME = 'username'
    SECTION_CREDENTIALS_PASSWORD = 'password'

    SECTION_DOWNLOAD = 'download'
    SECTION_DOWNLOAD_CLASS = 'class'

    CONFIG_FILE = 'download.cfg'

    def __init__(self):
        config = ConfigParser.ConfigParser()
        config.read(Config.CONFIG_FILE)
        self.username = config.get(Config.SECTION_CREDENTIALS, Config.SECTION_CREDENTIALS_USERNAME)
        self.password = config.get(Config.SECTION_CREDENTIALS, Config.SECTION_CREDENTIALS_PASSWORD)
        self.course = config.get(Config.SECTION_DOWNLOAD, Config.SECTION_DOWNLOAD_CLASS)


cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

r = opener.open('https://www.coursera.org/account/signin')
r = opener.open('https://www.coursera.org/maestro/auth/api/user/csrf_token')

#print "------------1>", cj

if True:
    csrfTokenValue = ''
    for ck in cj:
        if ck.name == 'csrf_token':
            csrfTokenValue = ck.value

    #print "Token value:", csrfTokenValue

    config = Config()
    formParams = {
        'email_address': config.username,
        'password': config.password,
        'csrf_token': csrfTokenValue
    }

    if True:
        formParams = urllib.urlencode(formParams)

        r = opener.open('https://www.coursera.org/maestro/auth/api/user/login', formParams)
        #print r.read()

        #r = opener.open('https://www.coursera.org/maestro/auth/api/user/login', formParams)
        #print "------------2>", cj
        #r = opener.open('https://www.coursera.org/')

        print cj

        r = opener.open('https://class.coursera.org/algo/auth/auth_redirector?type=login&subtype=normal&email=&visiting=%2Falgo%2Flecture%2Findex&minimal=true')

        r = opener.open(config.course)
        #print "------------3>", cj

        print r.read()


