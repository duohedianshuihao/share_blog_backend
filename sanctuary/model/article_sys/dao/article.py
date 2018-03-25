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
    def create(cls, title, content, status):
        return cls(title=title, content=content, status=status).save()

    @classmethod
    def get_article_detail(cls, id):
        return cls.get(id=id)

    @classmethod
    def update_n_read(cls, id):
        dao = cls.get(id=id)
        if not dao:
            return
        dao.n_read += 1
        return dao.save()

    @classmethod
    def paged_articles(cls, cursor, size):
        return list(cls.select().where(status=ArticleStatus.publishing).select()[cursor, cursor + size + 1])

    def update_article(self, title, content, update_time):
        now = datetime.datetime.now()
        return self.update(title=title, content=content, update_time=now).execute()
