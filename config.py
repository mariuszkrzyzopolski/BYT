class Config(object):
    DEBUG = True
    SECRET_KEY = "1"
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://sql11454497:RwkSDDxD8v@sql11.freemysqlhosting.net:3306' \
                              '/sql11454497 '
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER: 'localhost'
    MAIL_SERVER = 'smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USERNAME = '59193a4ea165c8'
    MAIL_PASSWORD = '6de17a5d4d0776'
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
