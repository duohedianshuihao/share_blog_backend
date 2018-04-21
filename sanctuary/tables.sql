CREATE TABLE `article_tag` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `article_id` smallint(5) unsigned NOT NULL,
    `tag_text` varchar(100) NOT NULL,
    `tag_hash` int(16) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `idx_article_id` (`article_id`),
    KEY `idx_tag_hash` (`tag_hash`)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `article_category` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `article_id` smallint(5) unsigned NOT NULL,
    `category_text` varchar(100) NOT NULL,
    `category_hash` int(16) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `idx_article_id` (`article_id`),
    KEY `idx_category_hash` (`category_hash`)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `article` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `title` varchar(100) NOT NULL,
    `content` blob NOT NULL,
    `n_read` int(10) unsigned DEFAULT 0,
    `status` tinyint(5) unsigned DEFAULT 0,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    PRIMARY KEY (`id`)
) DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;