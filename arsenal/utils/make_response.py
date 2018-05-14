# coding: utf-8

import simplejson
from flask import Response


def make_response(data, status_code=200):
    return Response(simplejson.dumps(data), mimetype='application/json', status=status_code)


def ok(content='', status_code=200):
    msg = {
        'status': 'ok',
        'content': content
    }
    resp = make_response(msg)
    return resp


def error(error="", status_code=400):
    msg = {
        'status': 'error',
        'msg': error
    }
    resp = make_response(msg, status_code=status_code)
    return resp
