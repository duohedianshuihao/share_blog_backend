# coding: utf-8

import datetime

from peewee import Model, SmallIntegerField, CharField, DateTimeField, fn
from gear.config import mysql_db


class TagDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'article_tag'

    id = SmallIntegerField(5)
    article_id = SmallIntegerField(5)
    tag_text = CharField(100)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_tag(cls, data):
        """data is a list of dict"""
        with cls._meta.database.atomic():
            for data_dict in data:
                cls.get_or_create(**data_dict)

    @classmethod
    def get_article_tags(cls, article_id):
        return list(cls.select().where(cls.article_id == article_id).execute())

    @classmethod
    def get_all_tags(cls):
        """rtype list(namedtuple)"""
        return list(cls.select(cls.tag_text, fn.COUNT(cls.id).alias('n_tag')).group_by(cls.tag_text).namedtuples())

    @classmethod
    def get_tag_all_articles(cls, tag_text):
        return list(cls.select().where(cls.tag_text == tag_text).execute())
