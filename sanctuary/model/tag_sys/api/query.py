# coding: utf-8

from ..dao.tag import TagDAO


def get_all_tag_article_ids(tag_text):
    tag_daos = TagDAO.get_all_tag_articles(tag_text)
    return [dao.article_id for dao in tag_daos]


get_article_tags = TagDAO.get_article_tags
n_tag_articles = TagDAO.get_n_tag
