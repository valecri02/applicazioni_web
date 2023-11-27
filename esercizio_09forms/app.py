from flask import Flask, render_template, request

app = Flask(__name__)

recensioni = [{'id':1, 'nomecognome': 'Juan Pablo Saenz', 'matricola': '241465', 'recensione': 'Molto buono!'}]

@app.route('/')
def index():
  first_plates = [{'id': 1, 'name': 'Pasta al tonno'},{'id': 2, 'name': 'Lasagne'}, {'id': 3, 'name': 'Pasta al sugo'}]
  return render_template('index.html', first=first_plates) 


@app.route('/recensioni')
def recensions():
  return render_template('recensioni.html', recensioni = recensioni)

# l'endpoint si aspetta delle richieste di tipo post
@app.route('/recensioni/new', methods = ['POST'])
def new_recensione():
  # si crea un dizionario che ha come key i nomi dei campi e value i valori inseriti dall'utente
  recensione = request.form.to_dict()

  if recensione['nomecognome'] == '':
    # necessario perché è anche possibile fare richieste senza usare l'interfaccia grafica (da un altro client)
    # tutte le verifiche vanno reimplementate dalla parte server
    app.logger.error('Il nome non può essere vuoto')
    return render_template('index.html') 
  if recensione['matricola'] == '':
    app.logger.error('La matricola non può essere vuota')
    return render_template('index.html') 
  if recensione['recensione'] == '':
    app.logger.error('La recensione non può essere vuota')
    return render_template('index.html') 

  foto = request.files['foto']
  foto.save('static/' + foto.filename)

  recensione['url_foto'] = foto.filename
  
  recensione['id'] = recensioni[-1]['id'] + 1
  recensioni.append(recensione)

  app.logger.info(recensioni)
  return render_template('index.html') 