# coding: utf-8

import datetime
from peewee import SmallIntegerField, CharField, DateTimeField, Model, DoesNotExist
from arsenal.user.util import hash_password
from sanctuary.models.user_sys.exception import EmailAlreadyUsed, InvalidPassword
from gear.config import mysql_db


class UserAuthDAO(Model):
    class Meta():
        database = mysql_db
        table_name = 'user_auth'

    id = SmallIntegerField(5)
    email = CharField(100)
    password = CharField(32)
    create_time = DateTimeField(default=datetime.datetime.now)
    update_time = DateTimeField(default=datetime.datetime.now)

    @classmethod
    def create_auth(cls, email, password):
        email = email.strip().lower()
        if not cls._check_available_email(email):
            raise EmailAlreadyUsed
        password = hash_password(password)
        return cls.create(email=email, password=password)

    @classmethod
    def verify_password(cls, uid, password):
        return cls.get(cls.id == uid).password == hash_password(password)

    @classmethod
    def _check_available_email(cls, email):
        '''
        check if the email is available
        @rtype: bool
        '''
        try:
            cls.get(cls.email == email)
        except DoesNotExist:
            return False
        else:
            return True

    def update_email(self, email):
        email = email.strip().lower()
        if self._check_available_email(email):
            return self.update(email=email)
        raise EmailAlreadyUsed

    def update_password(self, old_password, new_password):
        if self.password != hash_password(old_password):
            raise InvalidPassword
        return self.update(password=hash_password(new_password))
