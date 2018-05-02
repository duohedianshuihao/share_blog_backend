# coding: utf-8

import datetime
from schematics.types import IntType, DateTimeType, StringType
from schematics.models import Model

from arsenal.utils.datetime_util import _datetime


class UserDTO(Model):
    id = IntType()
    name = StringType(required=True, max_length=100)
    uuid = StringType(required=True, max_length=12)
    email = StringType(required=True)
    avatar = StringType(required=True)
    bits = IntType(required=True)
    create_time = DateTimeType(default=datetime.datetime.now)

    @classmethod
    def from_dao(cls, user_dao, user_auth_dao, uuid):
        return {
            'id': user_dao.id,
            'name': user_dao.name,
            'uuid': uuid,
            'avatar': user_dao.avatar,
            'email': user_auth_dao.email,
            'create_time': _datetime(user_dao.create_time)
        }
