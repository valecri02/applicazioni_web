import sqlite3

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
    WHERE P.id_utente = U.id AND P.id = ?'''

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_post, (id_post,))

    result = cursor.fetchone()

    cursor.close()
    connection.close()

    return result

def check_existing_post(id_post):
    query_post = 'SELECT id FROM post WHERE id = ?'

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_post, (id_post,))

    result = cursor.fetchone()

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