import sqlite3


def get_piatti():
    # define the query
    query_allpiatti = 'SELECT * FROM piatti'

    connection = sqlite3.connect('db/mangiato.db')

    # serve ad impostare un parametro sulla connessione: in questo caso converte da tupla a dizionario
    connection.row_factory = sqlite3.Row

    # cursor punta ai risultati che vengono restituiti dalla query
    # NOTA: deve essere definito un cursor per ciascuna query
    cursor = connection.cursor()
    # per eseguire la query
    cursor.execute(query_allpiatti)

    # prendi i risultati e chiudi la connessione
    # NOTA: result sarà una lista di tuple
    result = cursor.fetchall()
    print(result)

    cursor.close()
    connection.close()

    return result

def get_recensioni(id_piatto):
    # define the query
    query_recensioni_piatto = 'SELECT * FROM recensioni WHERE piatto = ?'

    connection = sqlite3.connect('db/mangiato.db')

    # serve ad impostare un parametro sulla connessione: in questo caso converte da tupla a dizionario
    connection.row_factory = sqlite3.Row

    # cursor punta ai risultati che vengono restituiti dalla query
    # NOTA: deve essere definito un cursor per ciascuna query
    cursor = connection.cursor()
    # per eseguire la query
    cursor.execute(query_recensioni_piatto, (id_piatto, ))

    # prendi i risultati e chiudi la connessione
    # NOTA: result sarà una lista di tuple
    result = cursor.fetchall()
    print(result)

    cursor.close()
    connection.close()

    return result

def add_recensione(recensione):
    # define the query
    query_recensioni_piatto = 'INSERT INTO recensioni(testo_recensione, url_foto, valutazione, piatto) VALUES (?, ?, ?, ?)'

    connection = sqlite3.connect('db/mangiato.db')

    # serve ad impostare un parametro sulla connessione: in questo caso converte da tupla a dizionario
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    # per eseguire la query

    success = False

    try:
        cursor.execute(query_recensioni_piatto, (recensione['testo_recensione'], recensione['url_foto'], recensione['valutazione'], recensione['piatto']))
        #in questo caso si fa un commit sulla connessione
        connection.commit()
        success = True
    except Exception as e:
        # se qualcosa non va bene 
        print('Error', str(e))
        #non salva nulla sul database
        connection.rollback()
    
    #qualsiasi sia il risultato si chiude il cursore e la connessione
    cursor.close()
    connection.close()

    return success