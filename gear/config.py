# coding: utf-8
import os


SECRET_KEY = os.environ.get('_SECRET_KEY')
DATABASE = os.environ.get('_DATABASE')
USER = os.environ.get('_USER')
PASSWD = os.environ.get('_PASSWORD')
HOST = os.environ.get('_HOST')
DB_PORT = int(os.environ.get('_PORT'))

TABLES = (
    'article_tag',
    'article_category',
    'article',
    'user',
    'user_auth',
    'user_uuid'
)
