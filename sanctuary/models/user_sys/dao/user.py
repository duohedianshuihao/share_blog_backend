# coding: utf-8

import datetime
from peewee import Model, SmallIntegerField, CharField, DateTimeField, BigIntegerField, DoesNotExist

from sanctuary.models.user_sys.exception import UserAlreadyExist
from sanctuary.models.user_sys.const import BITS_ADMIN

from gear.db_config import mysql_db
from arsenal.article.utils import get_hashed_value


class UserDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'user'

    id = SmallIntegerField(5)
    name = CharField(100)
    name_hash = BigIntegerField(16)
    avatar = CharField(100, default='')
    bits = BigIntegerField(20, default=0)  # set user roles
    create_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_user(cls, name):
        name_hash = get_hashed_value(name)
        if cls._check_available_name(name_hash):
            return cls.create(name=name, name_hash=name_hash)
        raise UserAlreadyExist  # view layer receive this exception

    @classmethod
    def get_user_by_uid(cls, uid):
        return cls.get_or_none(cls.id == uid)

    @classmethod
    def _check_available_name(cls, name_hash):
        '''
        check if the name is available
        @rtype: bool
        '''
        try:
            cls.get(cls.name_hash == name_hash)
        except DoesNotExist:
            return True
        else:
            return False

    def update_name(self, name):
        name_hash = get_hashed_value(name)
        if self._check_available_name(name_hash):
            return self.update(name=name, name_hash=name_hash).execute()  # return number of rows updated
        raise UserAlreadyExist

    def set_bit(self, bit):
        self.bits = self.bits | bit
        self.save()

    def check_bit(self, bit):
        return self.bits & bit

    def clear_bit(self, bit):
        self.bits = self.bits & (~bit)
        self.save

    def set_role_admin(self):
        self.set_bit(BITS_ADMIN)

    def is_user_admin(self):
        return self.check_bit(BIT)

    def revoke_role_admin(self):
        self.clear_bit(BITS_ADMIN)
