# coding: utf-8

import datetime
from peewee import Model, SmallIntegerField, CharField, DateTimeField
from base64 import urlsafe_b64decode, urlsafe_b64encode

from sanctuary.models.user_sys.const import USER_OFFSET
from gear.db_config import mysql_db


class UserUuidDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'user_uuid'

    id = SmallIntegerField(5)
    uuid = CharField(12)
    create_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_uuid(cls, uid):
        '''
        uuid's length should be 12
        '''
        big_id = uid + USER_OFFSET
        uuid = urlsafe_b64encode(str(big_id))
        dao = cls.get_or_none(cls.uuid == uuid)
        if dao:
            return
        return cls.create(uuid=uuid)

    @classmethod
    def get_uid_by_uuid(cls, uuid):
        uuid_dao = cls.get_or_none(cls.uuid == uuid)
        if not uuid_dao:
            return
        big_id = int(urlsafe_b64decode(uuid))  # uuid is str, which is c implemented, uuid_dao.uuid is unicode, which doesn't get 'buffer interface'
        return big_id - USER_OFFSET
