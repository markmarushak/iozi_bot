# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

from model import *
from db import *

m_search = ['жизнь', 'знакомства', 'холостяк', 'прибыль', 'незнакомец', 'заработок']
report = open('report.txt', 'a+')

def searchAddDb() :
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
    try:
        with conn.cursor() as cursor:
            cursor.execute(s_qeury)
            data = cursor.fetchall()
            for s in data:
                searchGroupID(s[0])

        conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
        with conn.cursor() as cursor:
            for gr in id_group:
                cursor.execute(i_group, (gr[0], gr[1]))

        conn.commit()

    finally:
        conn.close()



cursor.execute(s_group)
data = cursor.fetchall()
for d in data :
    try:
        postID(d)
    except:
        pass


for comment in id_post :
    try:
        addComment(comment)
    except:
        pass
