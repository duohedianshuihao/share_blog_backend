import os

from peewee import *


DATABASE = os.environ.get('_DATABASE')
USER = os.environ.get('_USER')
PASSWD = os.environ.get('_PASSWORD')
HOST = os.environ.get('_HOST')
PORT = int(os.environ.get('_PORT'))

mysql_db = MySQLDatabase(DATABASE, user=USER, password=PASSWD, host=HOST, port=PORT)
