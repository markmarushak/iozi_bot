#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import pymysql


# conn = pymysql.connect(host='185.74.252.15', port=3306, user='wladi984', passwd='uRvL98GUDi', db='wladi984_vkuser')
conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
cursor = conn.cursor()

i_group = "INSERT INTO groups (`id_group`, `name`) VALUES (%s,%s)"

s_group = "SELECT * FROM groups LIMIT 100, 10000"

i_qeury = "INSERT INTO query (`text`) VALUES (%s)"

s_qeury = "SELECT text FROM query"

s_user = "SELECT * FROM users"

s_posts = "SELECT * FROM temp_post"
i_posts = "insert INTO temp_post (`group_id`, `post_id`, `screen_name`) VALUES (%s, %s, %s)"

a_count = 0

aut = [
    {
        'count': 0,
        'account': [
            {'login': '79056363387','pass': 'TU3IIU'},
            {'login': '79025000549','pass': 'gOvv5BJM'},
            {'login': '79782601923','pass': '4pIZeLBu0x'},
            {'login': '79520028738','pass': 'WTFnx7'},
            {'login': '79104196601','pass': 'K120878r'},
            {'login': '79104301685','pass': 'Alesha123'},
            {'login': '79105736029','pass': '10121978a'},
        ]
    }
]

i_user = "INSERT INTO groups (`login`, `password`) VALUES (%s,%s)"
