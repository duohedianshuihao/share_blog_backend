# coding: utf-8

from sanctuary.models import article_sys


batch_get_articles = article_sys.batch_get_articles
batch_get_all_articles = article_sys.batch_get_all_articles
paged_articles = article_sys.paged_articles
paged_all_articles = article_sys.paged_all_articles
get_tag_all_articles = article_sys.get_tag_all_articles
get_category_all_articles = article_sys.get_category_all_articles
get_all_tags = article_sys.get_all_tags
get_all_categories = article_sys.get_all_categories

create_article = article_sys.create_article
update_article = article_sys.update_article
update_article_status = article_sys.update_article_status
update_n_read = article_sys.update_n_read
update_tag = article_sys.update_tag
update_category = article_sys.update_category
