import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # WTF Info
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess  '

    #SQL Alchemy Info
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or \
        'sqlite:///' + os.path.join(basedir, 'codeday.db3')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Mail Server Info
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['royalcows9@gmail.com']

    # Pagination Stuff
    POSTS_PER_PAGE = 7
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
