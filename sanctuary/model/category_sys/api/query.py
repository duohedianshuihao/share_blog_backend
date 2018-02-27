# coding: utf-8

from ..dao.category import CategoryDAO


def get_all_category_article_ids(category_text):
    category_daos = CategoryDAO.get_all_category_articles(category_text)
    return [dao.article_id for dao in category_daos]


get_article_categorys = CategoryDAO.get_article_categorys
n_category_articles = CategoryDAO.get_n_category
