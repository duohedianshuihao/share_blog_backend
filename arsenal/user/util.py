# coding: utf-8

from hashlib import sha256


def hash_password(id, string):
    return sha256("{}{}".format(id, string)).digest().decode('utf-8', 'ignore')
