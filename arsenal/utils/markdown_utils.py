# coding: utf-8

from houdini import h
from misaka import HtmlRenderer
from pygments import highlight
from pygments.formatters import HtmlFormatter, ClassNotFound
from pygments.lexers import get_lexer_by_name


class ArticleRenderer(HtmlRenderer):
    '''
    markdown 渲染器
    '''
    def blockcode(self, text, lang):
        try:
            lexer = get_lexer_by_name(lang)
        except ClassNotFound:
            lexer = None

        if lexer:
            formatter = HtmlFormatter()
            return highlight(text, lang, formatter)

        return "\n<pre><code>{}</code></pre>\n".format(h.escape_html(text.strip()))

    def blockquote(self, content):
        return "<blockquote>{}</blockquote>".format(content.strip())

    def header(self, content, level):
        if level <= 3:
            return "<h{}>{}</h{}>\n".format(level, content.strip(), level)
        return "<p>{}</p>\n".format(content.strip())

    def link(self, content, link, title=''):
        return "<a href='{link}'>{content}</a>".format(link=link, content=content.strip(), title=title)

    def autolink(self, link, is_email):
        if is_email:
            return link
        return self.link(content=link, link=link)
