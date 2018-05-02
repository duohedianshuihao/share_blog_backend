# coding: utf-8

import datetime
import simplejson

from schematics.types import IntType, DateTimeType, StringType
from schematics.types.compound import ModelType, ListType
from schematics.models import Model

from arsenal.utils.datetime_util import _datetime


class ContentDTO(Model):
    brief = StringType(required=True)
    detail = StringType()


class ArticleDTO(Model):
    id = IntType()
    title = StringType(required=True, max_length=100)
    content = ModelType(ContentDTO, required=True)
    n_read = IntType(required=True, default=0)
    status = IntType(required=True)
    tags = ListType(StringType)
    categories = ListType(StringType)
    create_time = DateTimeType(default=datetime.datetime.now)
    update_time = DateTimeType(default=datetime.datetime.now)

    @classmethod
    def from_dao(cls, dao, tag_daos, category_daos):
        return {
            'id': dao.id,
            'title': dao.title,
            'content': simplejson.loads(dao.content),
            'n_read': dao.n_read,
            'status': dao.status,
            'tags': [tag_dao.tag_text for tag_dao in tag_daos],
            'categories': [category_dao.category_text for category_dao in category_daos],
            'create_time': _datetime(dao.create_time),
            'update_time': _datetime(dao.update_time)
        }
