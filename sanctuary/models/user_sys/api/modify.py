# coding: utf-8

from ..dao.user import UserDAO
from ..dao.user_auth import UserAuthDAO
from ..dao.user_uuid import UserUuidDAO
from ..dto.user import UserDTO
from ..exception import UserNotExist

from gear.config import mysql_db


@mysql_db.atomic()
def create_user(name, email, password):
    user_dao = UserDAO.create_user(name)
    user_auth_dao = UserAuthDAO.create_auth(email, password)
    user_uuid_dao = UserUuidDAO.create_uuid(int(user_dao.id))
    return UserDTO.from_dao(user_dao, user_auth_dao, user_uuid_dao.uuid)


@mysql_db.atomic()
def update_user_info(uuid, name, email, password, new_password):
    uid = UserUuidDAO.get_uid_by_uuid(uuid)
    user_dao = _update_user_name(uid, name)
    user_auth_dao = _update_user_auth(uid, email, password, new_password)
    return UserDTO.from_dao(user_dao, user_auth_dao, uuid)


def _update_user_name(uid, name):
    user = UserDAO.get_user_by_uid(uid)
    if not user:
        raise UserNotExist
    return user.update_username(name) if name else user


def _update_user_auth(uid, email, password, new_password):
    user = UserAuthDAO.get_user_by_uid(uid)
    if not user:
        raise UserNotExist
    user = user.update_email(email) if email else user
    return user.update_password(password, new_password) if password and new_password else user


def set_role_admin(uuid):
    uid = UserUuidDAO.get_uid_by_uuid(uuid)
    user = UserDAO.get_user_by_uid(uid)
    if not user:
        return
    user.set_role_admin()


def revoke_role_admin(uuid):
    uid = UserUuidDAO.get_uid_by_uuid(uuid)
    user = UserDAO.get_user_by_uid(uid)
    if not user:
        return
    user.revoke_role_admin()
