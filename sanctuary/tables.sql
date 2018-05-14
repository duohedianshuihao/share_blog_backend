CREATE TABLE `article_tag` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `article_id` smallint(5) unsigned NOT NULL,
    `tag_text` varchar(100) NOT NULL,
    `tag_hash` bigint(16) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    `_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `idx_article_id` (`article_id`),
    KEY `idx_tag_hash` (`tag_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `article_category` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `article_id` smallint(5) unsigned NOT NULL,
    `category_text` varchar(100) NOT NULL,
    `category_hash` bigint(16) NOT NULL,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    `_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    KEY `idx_article_id` (`article_id`),
    KEY `idx_category_hash` (`category_hash`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `article` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `title` varchar(100) NOT NULL,
    `content` blob NOT NULL,
    `n_read` int(10) unsigned DEFAULT 0,
    `status` tinyint(5) unsigned DEFAULT 0,
    `create_time` datetime DEFAULT NULL,
    `update_time` datetime DEFAULT NULL,
    `_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `user` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `name_hash` bigint(16) NOT NULL,
    `avatar` varchar(100),
    `bits` bigint(20) unsigned NOT NULL DEFAULT '0',
    `create_time` datetime NULL,
    `_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;


CREATE TABLE `user_auth` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `email` varchar(100) NOT NULL,
    `password` varchar(32) DEFAULT NULL,
    `create_time` datetime NULL,
    `update_time` datetime NULL,
    `_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY `idx_email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

CREATE TABLE `user_uuid` (
    `id` smallint(5) unsigned NOT NULL AUTO_INCREMENT,
    `uuid` varchar(12) NOT NULL,
    `create_time` datetime NULL,
    `_created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `_updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`),
    UNIQUE KEY (`uuid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
