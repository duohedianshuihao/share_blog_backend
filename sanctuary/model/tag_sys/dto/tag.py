# coding: utf-8

import datetime

from schematics.types import IntType, DatetimeType, StringType
from schematics.models import Model

from arsenal.datetime_util import _datetime


class TagDTO(Model):
    id = IntType()
    article_id = IntType(required=True)
    tag_text = StringType(required=True, max_length=100)
    create_time = DatetimeType(default=datetime.datetime.now)
    update_time = DatetimeType(default=datetime.datetime.now)

    @classmethod
    def from_dao(cls, dao):
        return cls({
            'id': dao.id,
            'article_id': dao.article_id,
            'tag_text': dao.tag_text,
            'create_time': _datetime(dao.create_time),
            'update_time': _datetime(dao.update_time)
        })
