# -*- coding: utf-8 -*-
"""博客构建配置文件
"""

# For Maverick
site_prefix = "/Blog-With-GitHub-Boilerplate/"
source_dir = "../src/"
build_dir = "../dist/"
index_page_size = 10
archives_page_size = 20
enable_jsdelivr = {
    "enabled": False,
    "repo": ""
}

# 站点设置
site_name = "Stormycloudy"
site_logo = "${static_prefix}logo.png"
site_build_date = "2019-12-31T15:10-05:00"
author = "Shay L"
email = "xuecliu@iu.edu"
author_homepage = "https://pages.iu.edu/~xuecliu"
description = "Life is good."
key_words = ['ShayLiu', 'stormycloudy', 'atmosphericscience', 'blog']
language = 'En'
external_links = [
    {
        "name": "Maverick",
        "url": "https://github.com/AlanDecode/Maverick",
        "brief": "🏄‍ Go My Own Way."
    },
    {
        "name": "shay",
        "url": "https://pages.iu.edu/~xuecliu",
        "brief": "Stormycloudy's home page"
    }
]
nav = [
    {
        "name": "Home",
        "url": "${site_prefix}",
        "target": "_self"
    },
    {
        "name": "Archived",
        "url": "${site_prefix}archives/",
        "target": "_self"
    },
    {
        "name": "About",
        "url": "${site_prefix}about/",
        "target": "_self"
    }
]

social_links = [
    {
        "name": "Twitter",
        "url": "https://twitter.com/baroclinicat",
        "icon": "gi gi-twitter"
    },
    {
        "name": "GitHub",
        "url": "https://github.com/stormycloudy",
        "icon": "gi gi-github"
    },
    {
        "name": "linkedin",
        "url": "https://www.linkedin.com/in/shayliu/",
        "icon": "gi gi-linkedin-in"
    }
]

head_addon = r'''
<meta http-equiv="x-dns-prefetch-control" content="on">
<link rel="dns-prefetch" href="//cdn.jsdelivr.net" />
'''

footer_addon = ''

body_addon = ''
