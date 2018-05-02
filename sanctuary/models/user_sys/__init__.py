# coding: utf-8

from .api.query import (get_user_by_uuid, is_user_admin, verify_password)
from .api.modify import (create_user, update_user_info, set_role_admin, revoke_role_admin)

from .exception import UserNotExist, UserAlreadyExist, EmailAlreadyUsed


__all__ = [
    'get_user_by_uuid',
    'is_user_admin',
    'verify_password',

    'create_user',
    'update_user_info',
    'set_role_admin',
    'revoke_role_admin',

    'UserNotExist',
    'UserAlreadyExist',
    'EmailAlreadyUsed'
]
