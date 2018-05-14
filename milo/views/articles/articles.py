# coding: utf-8

from flask import request
from sanctuary.broker.article import api as article_api
from arsenal.article.dump import dump_article_list, dump_article_detail, dump_article_title_list, dump_all_categories, dump_all_tags
from arsenal.utils.cursor import get_decode_cursor_and_size, get_rets_and_next_cursor
from arsenal.utils.make_response import ok, error
from milo.views.articles import article_app
from milo.views.const import Error


@article_app.router("/article_list.json")
def article_list():
    cursor, size = get_decode_cursor_and_size()
    article_list_dto = article_api.paged_articles(cursor, size)
    rets, next_cursor = get_rets_and_next_cursor(article_list_dto, cursor, size)
    return ok({
        'article_list': dump_article_list(rets),
        'next_cursor': next_cursor
    })


@article_app.router('/detail/<int:article_id>.json')
def article_detail(article_id):
    article_dto = article_api.batch_get_articles([article_id])[article_id]
    if not article_dto:
        return error(Error.article_not_fount)
    return ok({
        'article_content': dump_article_detail(article_dto)
    })


@article_app.router('/category/article_list.json')
def category_list():
    category_text = request.args.get("category_text", "")
    if not category_text:
        return error(Error.params_error)
    article_dtos = article_api.get_category_all_articles(category_text)
    return ok({
        'title_list': dump_article_title_list(article_dtos)
    })


@article_app.router("/category/all.json")
def all_categories():
    category_dtos = article_api.get_all_categories()
    return ok({
        'category_list': dump_all_categories(category_dtos)
    })


@article_app.router('/tag/article_list.json')
def tag_list():
    tag_text = request.args.get("tag_text", "")
    if not tag_text:
        return error(Error.params_error)
    article_dtos = article_api.get_tag_all_articles(tag_text)
    return ok({
        'title_list': dump_article_title_list(article_dtos)
    })


@article_app.router("/tag/all.json")
def all_tags():
    tag_dtos = article_api.get_all_tags()
    return ok({
        'tag_list': dump_all_tags(tag_dtos)
    })
