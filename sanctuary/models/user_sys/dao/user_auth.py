# coding: utf-8

import datetime
from peewee import SmallIntegerField, CharField, DateTimeField, Model, DoesNotExist
from arsenal.user.util import hash_password
from sanctuary.models.user_sys.exception import EmailAlreadyUsed, InvalidPassword
from gear.db_config import mysql_db


class UserAuthDAO(Model):
    class Meta:
        database = mysql_db
        table_name = 'user_auth'

    id = SmallIntegerField(5)
    email = CharField(100)
    password = CharField(32)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_auth(cls, email, password):
        if not cls._check_available_email(email):
            raise EmailAlreadyUsed  # view layer receive this exception
        dao = cls.create(email=email)
        dao.update(password=hash_password(dao.id, password)).execute()
        return dao  # this dao does not contain password property

    @classmethod
    def verification(cls, uid, password):
        user = cls.get_user_by_uid(uid)
        if not user:
            return False
        return user.password == hash_password(uid, password)

    @classmethod
    def get_user_by_uid(cls, uid):
        return cls.get_or_none(cls.id == uid)

    @classmethod
    def _check_available_email(cls, email):
        '''
        check if the email is available
        @rtype: bool
        '''
        try:
            cls.get(cls.email == email)
        except DoesNotExist:
            return True
        else:
            return False

    def update_email(self, email):
        if self._check_available_email(email):
            return self.update(email=email)
        raise EmailAlreadyUsed  # view layer receive this exception

    def update_password(self, old_password, new_password):
        if self.password != hash_password(self.id, old_password):
            raise InvalidPassword  # view layer receive this exception
        return self.update(password=hash_password(self.id, new_password))
