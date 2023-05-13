import os

"""

Модуль с описанием конфигурации для приложения Flask

"""

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'SiteDB.db')
    SECRET_KEY = 'dslkghcfkblmdlrgjdrifcgsdgnckbjhdrtkjeskjgjhcfkgjfhgdrlkjg'