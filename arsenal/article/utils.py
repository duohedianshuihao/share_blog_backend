# coding: utf-8

from hashlib import md5
import misaka

from ..utils.markdown_utils import ArticleRenderer


def get_hashed_value(string):
    '''
    @rtype: int value with length of 16
    '''
    return int(md5(string).hexdigest(), 16) % (10 ** 16)


def _dump_para(text):
    md = misaka.Markdown(
        # skip-html - 跳过原文中的 HTML 代码
        # hard-wrap - 每个 \n 都渲染为 <br>
        renderer=ArticleRenderer(flags=('skip-html', 'hard-wrap')),
        # space-headers - 只将 # Title 转为 <header>
        #                 #Title 会保持原样
        extensions=('disable-indented-code', 'autolink', 'space-headers'))

    return {
        'type': 'text',
        'text': text,
        'html': md(text)
    }
