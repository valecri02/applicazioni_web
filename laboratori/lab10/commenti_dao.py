import sqlite3

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

def add_comment(commento):
    query_post = 'INSERT INTO commenti (data_pubblicazione, testo, id_post, id_utente, valutazione, immagine) VALUES (?, ?, ?, ?, ?, ?)'
 
    connection = sqlite3.connect('db/social.db')
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    success = False

    try:
        cursor.execute(query_post, (commento['data_pubblicazione'], commento['testo'], commento['id_post'], commento['id_utente'], commento['valutazione'], commento['immagine']))
        connection.commit()
        success = True
        print("Elemento aggiunto!!")
    except Exception as e:
        print('Error', str(e))
        connection.rollback()
    
    cursor.close()
    connection.close()

    return success