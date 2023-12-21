import sqlite3

def get_users():
    query_utenti = 'SELECT * FROM utenti'

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute(query_utenti)

    result = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return result

def get_user_by_id(id_utente):
    query = 'SELECT * FROM utenti WHERE id = ?'
    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query, (id_utente, ))

    result = cursor.fetchone()
    print(result)

    cursor.close()
    connection.close()

    return result

def creare_utente(nuovo_utente):
    query = 'INSERT INTO utenti(nickname, password, immagine_profilo) VALUES (?,?,?)'

    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    success = False

    try:
        cursor.execute(query, (nuovo_utente['nickname'], nuovo_utente['password'], nuovo_utente['immagine_profilo']))
        connection.commit()
        success = True
    except Exception as e:
        print('Error', str(e))
        connection.rollback()

    cursor.close()
    connection.close()

    return success

def get_user_by_nickname(nickname):
    esiste_gia = False

    query = 'SELECT * FROM utenti WHERE nickname = ?'
    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()

    cursor.execute(query, (nickname, ))

    result = cursor.fetchone()
    print(result)

    cursor.close()
    connection.close()

    return result