# coding: utf-8

from ..dao.user import UserDAO
from ..dao.user_auth import UserAuthDAO
from ..dao.user_uuid import UserUuidDAO
from ..dto.user import UserDTO


def get_user_by_uuid(uuid):
    uid = UserUuidDAO.get_uid_by_uuid(uuid)
    user_dao = UserDAO.get_user_by_uid(uid)
    if not user_dao:
        return
    user_auth_dao = UserAuthDAO.get_user_by_uid(int(user_dao.id))
    if not user_auth_dao:
        return
    return UserDTO.from_dao(user_dao, user_auth_dao, uuid)


def is_user_admin(uuid):
    uid = UserUuidDAO.get_uid_by_uuid(uuid)
    user_dao = UserAuthDAO.get_user_by_uid(uid)
    if not user_dao:
        return
    return user_dao.is_user_admin()


def verify_password(uuid, password):
    uid = UserUuidDAO.get_uid_by_uuid(uuid)
    return UserAuthDAO.verification(uid, password)
