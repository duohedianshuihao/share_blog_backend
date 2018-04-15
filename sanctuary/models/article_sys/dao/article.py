# coding: utf-8

import datetime

from peewee import Model, CharField, SmallIntegerField, DateTimeField, BlobField, IntegerField
from gear.config import mysql_db

from ..const import ArticleStatus


class ArticleDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'article'

    id = SmallIntegerField(5)
    title = CharField(100)
    content = BlobField()
    n_read = IntegerField(10)
    status = SmallIntegerField(5)
    create_time = DateTimeField(default=datetime.datetime.now())
    update_time = DateTimeField(default=datetime.datetime.now())

    @classmethod
    def create_article(cls, title, content, status):
        '''content is a dict'''
        return cls.create(title=title, content=content, status=status)  # cls.().save() in peewee dont reture dao but only int

    @classmethod
    def get_article_detail(cls, id):
        """filter article status on different batch or page methods"""
        return cls.get_or_none(cls.id == id)

    @classmethod
    def batch_get_articles(cls, ids):
        d = {id: None for id in ids}
        daos = list(cls.select().where(cls.id.in_(ids) and cls.status == ArticleStatus.published).execute())
        for dao in daos:
            if not dao:
                continue
            d[dao.id] = dao
        return d

    @classmethod
    def batch_get_all_articles(cls, ids):
        """this only for superuser"""
        d = {id: None for id in ids}
        daos = list(cls.select().where(cls.ids.in_(ids)).execute())
        for dao in daos:
            if not dao:
                continue
            d[dao.id] = dao
        return d

    @classmethod
    def update_n_read(cls, id):
        return cls.update(n_read=cls.n_read + 1).where(cls.id == id).execute()

    @classmethod
    def paged_articles(cls, cursor, size):
        return list(cls.select().where(cls.status == ArticleStatus.published).order_by(cls.create_time.desc()).execute())[cursor: cursor + size + 1]

    @classmethod
    def paged_all_articles(cls, cursor, size):
        """this only for superuser"""
        return list(cls.select().order_by(cls.create_time.desc()))[cursor: cursor + size + 1]

    def update_article(self, title, content, update_time):
        now = datetime.datetime.now()
        return self.update(title=title, content=content, update_time=now).execute()

    def update_article_status(self, status):
        return self.update(status=status).execute()
