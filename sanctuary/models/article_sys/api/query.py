# coding: utf-8

from ..dao.article import ArticleDAO
from ..dao.category import CategoryDAO
from ..dao.tag import TagDAO

from ..dto.article import ArticleDTO


def _build_article_dto_by_dao(dao):
    tag_daos, category_daos = TagDAO.get_article_tags(dao.id), CategoryDAO.get_article_categories(dao.id)
    return ArticleDTO.from_dao(dao, tag_daos, category_daos)


def batch_get_articles(article_ids):
    if not article_ids:
        return {}
    d = {article_id: None for article_id in article_ids}
    article_daos_d = ArticleDAO.batch_get_articles(article_ids)
    for article_id in article_ids:
        if not article_daos_d[article_id]:
            continue
        d[article_id] = _build_article_dto_by_dao(article_daos_d[article_id])
    return d


def batch_get_all_articles(article_ids):
    if not article_ids:
        return {}
    d = {article_id: None for article_id in article_ids}
    article_daos_d = ArticleDAO.batch_get_all_articles(article_ids)
    for article_id in article_ids:
        if not article_daos_d[article_id]:
            continue
        d[article_id] = _build_article_dto_by_dao(article_daos_d[article_id])
    return d


def paged_articles(cursor, size):
    daos = ArticleDAO.paged_articles(cursor, size)
    return [_build_article_dto_by_dao(dao) for dao in daos]


def paged_all_articles(cursor, size):
    daos = ArticleDAO.paged_all_articles(cursor, size)
    return [_build_article_dto_by_dao(dao) for dao in daos]


def get_tag_all_articles(tag_text):
    daos = TagDAO.get_tag_all_articles(tag_text)
    if not daos:
        return {}
    article_ids = [dao.article_id for dao in daos]
    article_d = batch_get_articles(article_ids)
    return sorted(filter(None, article_d.values()), key=lambda x: x.create_time, reverse=True)  # filter unpublished articles


def get_category_all_articles(category_text):
    daos = CategoryDAO.get_category_all_articles(category_text)
    if not daos:
        return {}
    article_ids = [dao.article_id for dao in daos]
    article_d = batch_get_articles(article_ids)
    return sorted(filter(None, article_d.values()), key=lambda x: x.create_time, reverse=True)


get_all_tags = TagDAO.get_all_tags
get_all_categories = CategoryDAO.get_all_categories
