import vk_api
from db import *

def selectDB() :
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
    query = "SELECT login,password FROM users"
    try:
        with conn.cursor() as cursor:
            cursor.execute(query)
            data = cursor.fetchall()
            for s in data:
                auth(s[0],[1])

    finally:
        conn.close()

def auth(login,password) :
    stat = 0
    try :
        vk_session = vk_api.VkApi(login, password)
        vk_session.auth()
        v_k = vk_session.get_api()
        stat = 1
        return v_k
    except:
        stat = 0

    if stat == 1 :
        print("работает")
    else:
        print('не работает', login)



selectDB()