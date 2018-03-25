# coding: utf-8

import datetime

from peewee import Model, SmallIntegerField, CharField, DateTimeField
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
    def create(cls, article_id, tag_text):
        dao = cls.select().where(cls.article_id == article_id, cls.tag_text == tag_text).select()
        if dao:
            return
        return cls(article_id=article_id, tag_text=tag_text).save()

    @classmethod
    def get_article_tags(cls, article_id):
        return list(cls.select().where(cls.article_id == article_id).select())

    @classmethod
    def get_all_tag_articles(cls, tag_text):
        return cls.select().where(cls.tag_text == tag_text).select()

    @classmethod
    def get_n_tag(cls, tag_text):
        return cls.select().where(cls.tag_text == tag_text).count()
