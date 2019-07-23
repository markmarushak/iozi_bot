import vk_api
from db import *

id_group = []
id_post  = []
a_count = [
    {'count':0}
]

def getCount(db) :
    if a_count[0]['count'] == len(db):
        setCount(0)
    else:
        plusCount(1)
    return a_count[0]['count']

def setCount(x):
    a_count[0]['count'] = x

def plusCount(x):
    a_count[0]['count'] = a_count[0]['count'] + x

def users() :
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
    try:
        with conn.cursor() as cursor:
            cursor.execute(s_user)
            data = cursor.fetchall()

        return data
    finally:
        conn.close()

def auth() :
    userc = users()
    count = getCount(userc)
    login = userc[count][1]
    password = userc[count][2]



    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()
    v_k = vk_session.get_api()

    print('connect account')
    return v_k

vk = auth()


def checkIsClose(key) :
    value = key.get('is_closed')
    if value == 0 :
        return 'true'
    else :
        return 'false'

def addComment(post) :
    data = 0
    try:
        vk.wall.createComment(owner_id=-post[0] ,post_id=id, message='ЗНАЕМ ВСЁ ПРО ВСЕХ. ОБРАЩАЙТЕСЬ. https://in-touch.ooo')
        data =1
        print(post[0], "коменнтарий в эту грппу")
    except:
        data=0

    if data == 0:
        auth()
        vk.wall.createComment(owner_id=-post[0], post_id=post[1], message='ЗНАЕМ ВСЁ ПРО ВСЕХ. ОБРАЩАЙТЕСЬ. https://in-touch.ooo')
        print(post[0], "коменнтарий в эту грппу")



def postID(groups) :
    data = 0
    ow_id = -groups[1]
    try:
        data = vk.wall.get(owner_id=ow_id, count=10, offset=0)
    except :
        pass

    if data == 0:
        auth()
        data = vk.wall.get(owner_id=-groups[1], count=10, offset=0)

    if data != 0 :
        for key in data['items']:
            id_post = ({0: key.get('owner_id'), 1: key.get('id'), 2: groups[3]})
            postAddDb(id_post)

def searchGroupID(word) :
    search = vk.groups.search(q=word, count=1000, offset=0)
    for key in search['items']:
        if (checkIsClose(key)) :
            id_group.append({0: key.get('id'), 1: key.get('screen_name')})


def postAddDb(data) :
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='', db='dbot')
    try:
        with conn.cursor() as cursor:
            for gr in data:
                cursor.execute(i_posts, (gr[0], gr[1], gr[2]))

        conn.commit()

    finally:
        conn.close()

