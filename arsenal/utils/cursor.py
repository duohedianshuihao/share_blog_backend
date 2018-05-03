# coding: utf-8

from flask import request
from base64 import urlsafe_b64encode, urlsafe_b64decode


def get_decode_cursor_and_size(cursor='', size=10):
    cursor_str = request.args.get('cursor', cursor).strip()
    size = request.args.get('size', size)
    cursor = urlsafe_b64decode(cursor_str.encode('utf-8'))
    return int(cursor), int(size)


def get_rets_and_next_cursor(objs, cursor, size):
    if len(objs) == size + 1:
        next_cursor = urlsafe_b64encode(cursor + size)
        objs = list(objs)[:-1]
        return objs, next_cursor
    return objs, ''
