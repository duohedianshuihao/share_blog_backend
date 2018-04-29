# coding: utf-8


class UserAlreadyExist(Exception):
    '''用户已经存在'''
    pass


class EmailAlreadyUsed(Exception):
    '''邮箱已经注册'''
    pass


class UserNotExist(Exception):
    '''用户已经存在'''
    pass


class InvalidPassword(Exception):
    '''密码不正确'''
    pass
