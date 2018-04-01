# coding: utf-8

import datetime

from peewee import Model, SmallIntegerField, CharField, DateTimeField, fn
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
    def create_category(cls, data):
        """data is a list of dict"""
        with cls._meta.database.atomic():
            for data_dict in data:
                cls.get_or_create(**data_dict)

    @classmethod
    def get_article_categories(cls, article_id):
        return list(cls.select().where(cls.article_id == article_id).execute())

    @classmethod
    def get_all_categories(cls):
        """rtype list(namedtuples)"""
        return list(cls.select(cls.category_text, fn.COUNT(cls.id).alias('n_category')).group_by(cls.category_text).namedtuples())

    @classmethod
    def get_category_all_articles(cls, category_text):
        return list(cls.select().where(cls.category_text == category_text).execute())
