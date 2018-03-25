# coding: utf-8

import datetime
import simplejson

from schematics.types import IntType, DatetimeType, StringType
from schematics.types.compound import ModelType
from schematics.models import Model

from arsenal.datetime_util import _datetime


class ContentDTO(Model):
    brief = StringType()
    detail = StringType()


class ArticleDTO(Model):
    id = IntType()
    title = StringType(required=True, max_length=100)
    content = ModelType(ContentDTO, required=True)
    n_read = IntType(required=True)
    status = IntType(required=True)
    create_time = DatetimeType(required=True, default=datetime.datetime.now)
    update_time = DatetimeType(required=True, default=datetime.datetime.now)

    @classmethod
    def from_dao(cls, dao):
        return {
            'id': dao.id,
            'title': dao.title,
            'content': simplejson.loads(dao.content),
            'n_read': dao.n_read,
            'status': dao.status,
            'create_time': _datetime(dao.create_time),
            'update_time': _datetime(dao.update_time)
        }
