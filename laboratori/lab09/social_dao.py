import sqlite3

def get_users():
    query_utenti = 'SELECT id, nickname FROM utenti'

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_utenti)

    result = cursor.fetchall()
    print(result)

    cursor.close()
    connection.close()

    return result

def get_posts():
    query_posts = '''SELECT P.id, data_pubblicazione, testo, immagine_post, id_utente, nickname, immagine_profilo
    FROM post P, utenti U
    WHERE P.id_utente = U.id
    ORDER BY data_pubblicazione DESC'''

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_posts)

    result = cursor.fetchall()

    cursor.close()
    connection.close()

    return result


def get_single_post(id_post):
    query_post = '''SELECT P.id, data_pubblicazione, testo, immagine_post, id_utente, nickname, immagine_profilo
    FROM post P, utenti U
    WHERE P.id_utente = U.id AND P.id = ?
    ORDER BY data_pubblicazione'''

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_post, (id_post,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

def get_post_comments(id_post):
    query_comment = '''SELECT C.id, data_pubblicazione, testo, nickname, immagine, valutazione
    FROM commenti C, utenti U
    WHERE id_post = ? AND U.id = C.id_utente
    ORDER BY C.data_pubblicazione DESC'''

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_comment, (id_post,))

    result = cursor.fetchall()
    print(id_post, result)

    cursor.close()
    connection.close()

    return result

def add_post(post):
    query_post = 'INSERT INTO post(data_pubblicazione, testo, immagine_post, id_utente, data_sort) VALUES (?, ?, ?, ?, ?)'

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    success = False

    try:
        cursor.execute(query_post, (post['data_pubblicazione'], post['testo'], post['immagine_post'], post['id_utente'], post['data_sort']))
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()
    
    cursor.close()
    connection.close()

    return success


def add_comment(commento, user, img):
    if user and img:
        query_post = 'INSERT INTO commenti(data_pubblicazione, testo, id_post, id_utente, valutazione, immagine) VALUES (?, ?, ?, ?, ?, ?)'
    elif img:
        query_post = 'INSERT INTO commenti(data_pubblicazione, testo, id_post, valutazione, immagine) VALUES (?, ?, ?, ?, ?)'
    elif user:
        query_post = 'INSERT INTO commenti(data_pubblicazione, testo, id_post, id_utente, valutazione) VALUES (?, ?, ?, ?, ?)'
    else:
        query_post = 'INSERT INTO commenti(data_pubblicazione, testo, id_post, valutazione) VALUES (?, ?, ?, ?)'
    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    success = False

    try:
        if user:
            cursor.execute(query_post, (commento['data_pubblicazione'], commento['testo'], commento['id_post'], commento['id_utente'], commento['valutazione'], commento['immagine']))
        elif img:
            cursor.execute(query_post, (commento['data_pubblicazione'], commento['testo'], commento['id_post'], commento['valutazione'], commento['immagine']))
        elif user:
            cursor.execute(query_post, (commento['data_pubblicazione'], commento['testo'], commento['id_post'], commento['id_utente'], commento['valutazione']))
        else:
            cursor.execute(query_post, (commento['data_pubblicazione'], commento['testo'], commento['id_post'], commento['valutazione']))
        
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()
    
    cursor.close()
    connection.close()

    return success

def check_existing_user(nickname):
    query_user = "SELECT id, nickname FROM utenti WHERE nickname = ?"

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_user, (nickname,))

    result = cursor.fetchone()
    print(result)

    cursor.close()
    connection.close()

    return result

def add_user(user):
    query_post = 'INSERT INTO utenti(nickname) VALUES (?)'

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    success = False

    try:
        cursor.execute(query_post, (user['nickname'],))
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()
    
    cursor.close()
    connection.close()

    return success