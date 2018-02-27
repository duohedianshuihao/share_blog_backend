CREATE TABLE `article_tag` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `article_id` smallint(5) unsigned NOT NULL,
    `tag_text` varchar(100) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `article_id` (`article_id`)
);


CREATE TABLE `article_category` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `article_id` smallint(5) unsigned NOT NULL,
    `category_text` varchar(100) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `article_id` (`article_id`)
);


CREATE TABLE `article` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `title` varchar(100) NOT NULL,
    `content` blob NOT NULL,
    `n_read` smallint(5) unsigned DEFAULT 0,
    `is_published` smallint(5) unsigned DEFAULT 0,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
);