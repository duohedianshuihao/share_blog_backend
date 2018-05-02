# coding: utf-8
import simplejson as json
from ..dao.article import ArticleDAO
from ..dao.tag import TagDAO
from ..dao.category import CategoryDAO
from ..dto.article import ArticleDTO
from ..dto.tag import TagDTO
from ..dto.category import CategoryDTO

from ..const import ArticleStatus

from ..api.query import _build_article_dto_by_dao
from gear.config import mysql_db
from arsenal.article.utils import get_hashed_value


@mysql_db.atomic()
def create_article(title, brief, detail, tags, categories, status=ArticleStatus.on_edit):
    article_dto = _new_article(title, brief, detail, status)
    tag_dtos = _new_tags(article_dto.id, tags)
    categories_dtos = _new_categories(article_dto.id, categories)
    article_dto.tags = [dto.tag_text for dto in tag_dtos]
    article_dto.categories = [dto.category_text for dto in categories_dtos]
    return article_dto


def update_article_status(article_id, status):
    dao = ArticleDAO.get_article_detail(article_id)
    if not dao:
        return
    dao.update_article_status(status)
    return _build_article_dto_by_dao(dao)


def update_article(article_id, title, brief, detail):
    content = {
        'brief': brief,
        'detail': detail
    }
    dao = ArticleDAO.get_article_detail(article_id)
    if not dao:
        return
    dao.update_article(title, content)
    return _build_article_dto_by_dao(dao)


def _new_article(title, brief, detail, status):
    content = {
        'brief': brief,
        'detail': detail
    }
    article_dto = ArticleDTO({
        'title': title,
        'content': content,
        'status': status
    })

    article_dto.validate()
    content_d = article_dto.content.to_native()
    dao = ArticleDAO.create_article(article_dto.title, json.dumps(content_d), article_dto.status)
    article_dto.id = dao.id
    return article_dto


def _new_tags(article_id, tags):
    data = map(lambda tag: {'tag_text': tag, 'article_id': article_id, 'tag_hash': get_hashed_value(tag)}, tags)
    daos = TagDAO.create_tag(data)
    return map(TagDTO.from_dao, [dao[0] for dao in daos])


def _new_categories(article_id, categories):
    data = map(lambda category: {'category_text': category, 'article_id': article_id, 'category_hash': get_hashed_value(category)}, categories)
    daos = CategoryDAO.create_category(data)
    return map(CategoryDTO.from_dao, [dao[0] for dao in daos])


def update_tag(old_tag, tag_text):
    if old_tag == tag_text:
        return
    TagDAO.update_tag(old_tag, tag_text)


def update_category(old_category, category_text):
    if old_category == category_text:
        return
    CategoryDAO.update_category(old_category, category_text)


update_n_read = ArticleDAO.update_n_read
