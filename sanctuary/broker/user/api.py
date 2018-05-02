# coding: utf-8

from sanctuary.models import user_sys
from gear.config import mysql_db


@mysql_db.atomic()
def create_user(name, email, password):
    email = email.strip().lower()
    return user_sys.create_user(name, email, password)


@mysql_db.atomic()
def update_user(uuid, name=None, email=None, password=None, new_password=None):
    if not uuid:
        return
    return user_sys.update_user_info(uuid, name, email, password, new_password)


def login(uuid, password):
    if user_sys.verify_password(uuid, password):
        return user_sys.get_user_by_uuid(uuid)
    return


is_user_admin = user_sys.is_user_admin
set_role_admin = user_sys.set_role_admin
revoke_role_admin = user_sys.revoke_role_admin
