# coding: utf-8

import datetime


def _datetime(d):
    if isinstance(d, datetime.datetime):
        return d
    if isinstance(d, datetime.date):
        return datetime.datetime(d.year, d.month, d.day)
    try:
        n = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
    except ValueError:
        try:
            n = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
        except ValueError:
            try:
                n = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M')
            except ValueError:
                n = datetime.datetime.strptime(d, '%Y-%m-%d')
    return n
