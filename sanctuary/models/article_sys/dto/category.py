# coding: utf-8

import datetime

from schematics.types import IntType, DateTimeType, StringType
from schematics.models import Model

from arsenal.datetime_util import _datetime


class CategoryDTO(Model):
    id = IntType()
    article_id = IntType(required=True)
    category_text = StringType(required=True, max_length=100)
    create_time = DateTimeType(default=datetime.datetime.now)
    update_time = DateTimeType(default=datetime.datetime.now)

    @classmethod
    def from_dao(cls, dao):
        return cls({
            'id': dao.id,
            'article_id': dao.article_id,
            'category_text': dao.category_text,
            'create_time': _datetime(dao.create_time),
            'update_time': _datetime(dao.update_time)
        })
