# coding: utf-8

import hashlib


def get_hashed_value(string):
    '''
    @rtype: int value with length of 16
    '''
    return int(hashlib.sha256(string).hexdigest(), 16) % (10 ** 16)
