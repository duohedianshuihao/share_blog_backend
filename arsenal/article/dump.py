# coding: utf-8


def dump_article_list(dtos):
    if not dtos:
        return []
    return [dump_article_brief(dto) for dto in dtos]


def dump_article_brief(dto):
    if not dto:
        return {}
    return {
        'id': dto.id,
        'title': dto.title,
        'brief': dto.content.brief,
        'n_read': dto.n_read,
        'tages': dto.tags,
        'categories': dto.categories,
        'create_time': dto.create_time,
        'update_time': dto.updatetime
    }


def dump_article_title_list(dtos):
    if not dtos:
        return []
    return [{
        'id': dto.id,
        'title': dto.title,
        'create_time': dto.create_time
    } for dto in dtos]


def dump_article_detail(dto):
    if not dto:
        return {}
    brief_dto = dump_article_brief(dto)
    brief_dto.update({
        'detail': dto.content.detail
    })
    return brief_dto


def dump_all_categories(dtos):
    if not dtos:
        return []
    return [{
        'category': dto.category_text,
        'n_category': dto.n_category
    } for dto in dtos]


def dump_all_tags(dtos):
    if not dtos:
        return []
    return [{
        'tag': dto.tag_text,
        'n_tag': dto.n_tag
    } for dto in dtos]
