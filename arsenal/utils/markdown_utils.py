# coding: utf-8

import misaka
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name

class ArticleRenderer(misaka.HtmlRenderer):
    '''
    markdown 渲染器
    '''

    def blockquote(self, content):
        return "<blockquote>{}</blockquote>".format(content.strip())

