# coding: utf-8

import datetime

from peewee import *
from gear.config import mysql_db


class CategoryDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'article_category'

    id = SmallIntegerField(5)
    article_id = SmallIntegerField(5)
    category_text = CharField(100)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create(cls, article_id, category_text):
        dao = cls.select().where(cls.article_id == article_id, cls.category_text == category_text).select()
        if dao:
            return
        return cls(article_id=article_id, category_text=category_text).save()

    @classmethod
    def get_article_categories(cls, article_id):
        return list(cls.select().where(cls.article_id == article_id).select())

    @classmethod
    def get_all_category_articles(cls, category_text):
        return cls.select().where(cls.category_text == category_text).select()

    @classmethod
    def get_n_category(cls, category_text):
        return cls.select().where(cls.category_text == category_text).count()
