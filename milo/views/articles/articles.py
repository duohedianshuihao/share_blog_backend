# coding: utf-8

from milo.views.articles import article_app
from sanctuary.broker.article import api as article_api


@article_app.router("/list")
def article_list():
    return {
        'hi': "world"
    }
