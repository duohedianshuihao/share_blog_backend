# coding: utf-8

import datetime

from peewee import Model, IntegerField, SmallIntegerField, CharField, DateTimeField, fn
from gear.config import mysql_db
from arsenal.article.utils import get_hashed_value


class TagDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'article_tag'

    id = SmallIntegerField(5)
    article_id = SmallIntegerField(5)
    tag_text = CharField(100)
    tag_hash = IntegerField(16)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_tag(cls, data):
        """
        data is a list of dict
        @rtype is a list of tuple like (dao, bool)
        """
        daos = []
        with cls._meta.database.atomic():
            for data_dict in data:
                daos.append(cls.get_or_create(**data_dict))
        print daos
        return daos

    @classmethod
    def get_article_tags(cls, article_id):
        return list(cls.select().where(cls.article_id == article_id).execute())

    @classmethod
    def get_all_tags(cls):
        """rtype list(namedtuple)"""
        return list(cls.select(cls.tag_text, fn.COUNT(cls.id).alias('n_tag')).group_by(cls.tag_hash).namedtuples())

    @classmethod
    def get_tag_all_articles(cls, tag_text):
        tag_hash = get_hashed_value(tag_text)
        return list(cls.select().where(cls.tag_hash == tag_hash).execute())

    @classmethod
    def update_tag(cls, old_tag, tag_text):
        old_hash = get_hashed_value(old_tag)
        daos = list(cls.select().where(cls.tag_hash == old_hash).execute())
        if not daos:
            return
        new_hash = get_hashed_value(tag_text)
        map(lambda dao: dao.update(cls.tag_text=tag_text, cls.tag_hash=new_hash).execute(), daos)
