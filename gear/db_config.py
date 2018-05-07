# coding: utf-8

from config import (DATABASE, USER, PASSWD, HOST, DB_PORT)

from peewee import *

mysql_db = MySQLDatabase(DATABASE, user=USER, password=PASSWD, host=HOST, port=DB_PORT)
