# coding: utf-8

import datetime

from peewee import Model, BigIntegerField, SmallIntegerField, CharField, DateTimeField, fn
from gear.config import mysql_db
from arsenal.article.utils import get_hashed_value


class CategoryDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'article_category'

    id = SmallIntegerField(5)
    article_id = SmallIntegerField(5)
    category_text = CharField(100)
    category_hash = BigIntegerField(16)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_category(cls, data):
        """
        data is a list of dict
        @rtype is a list of tuple like (dao, bool)
        """
        daos = []
        with cls._meta.database.atomic():
            for data_dict in data:
                daos.append(cls.get_or_create(**data_dict))
        return daos

    @classmethod
    def get_article_categories(cls, article_id):
        return list(cls.select().where(cls.article_id == article_id).execute())

    @classmethod
    def get_all_categories(cls):
        """rtype list(namedtuples)"""
        return list(cls.select(cls.category_text, fn.COUNT(cls.id).alias('n_category')).group_by(cls.category_hash).namedtuples())

    @classmethod
    def get_category_all_articles(cls, category_text):
        category_hash = get_hashed_value(category_text)
        return list(cls.select().where(cls.category_hash == category_hash).execute())

    @classmethod
    def update_category(cls, old_category, category_text):
        old_hash = get_hashed_value(old_category)
        daos = cls.select().where(cls.category_hash == old_hash).execute()
        if not daos:
            return
        new_hash = get_hashed_value(category_text)
        map(lambda dao: dao.update(category_text=category_text, category_hash=new_hash).execute(), daos)
