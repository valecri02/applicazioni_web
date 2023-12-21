# import module
from flask import Flask, render_template, request, redirect, url_for
import piatti_dao, utenti_dao
from flask_login import LoginManager, login_user, login_required, logout_user
from models import User
from flask_session import Session
from werkzeug.security import generate_password_hash, check_password_hash


# create the application
app = Flask(__name__)
# SECRET KEY: testo che conosce solo lo sviluppatore che viene usato per generare la codifica dei dati che vengono mandati
# usato per fare l'encripting dei dati
app.config['SECRET_KEY'] = 'qualsiasi valore'

#creo un istanza di quel login manager
login_manager = LoginManager()
login_manager.init_app(app)   #viene inizializzato per riconoscere la nostra app

# define the homepage
@app.route('/')
def index():
  piatti_db = piatti_dao.get_piatti()
  return render_template('index.html', piatti=piatti_db)

@app.route('/piatti/<int:id>')
def piatto_singolo(id):
  piatto_db = piatti_dao.get_piatto(id)
  recensioni_db = piatti_dao.get_recensioni(id)
  return render_template('single.html', piatto = piatto_db, recensioni=recensioni_db)

# define the about page
@app.route('/about')
def about():
  return render_template('about.html')

# define the signup page
@app.route('/iscriviti')
def iscriviti():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():

  new_user_from_form = request.form.to_dict()

  if new_user_from_form ['nome'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))
  if new_user_from_form ['cognome'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))
  if new_user_from_form ['email'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))
  if new_user_from_form ['password'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))
  
  new_user_from_form['password'] = generate_password_hash(new_user_from_form['password'])

  success = utenti_dao.creare_utente(new_user_from_form)

  if success:
    return redirect(url_for('index'))
  
  return redirect(url_for('iscriviti'))


@app.route('/login', methods=['POST'])
def login():

  utente_form = request.form.to_dict()

  if utente_form ['email'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))
  if utente_form ['password'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))

  utente_db = utenti_dao.get_user_by_email(utente_form['email'])

  if not utente_db or not check_password_hash(utente_db['password'], utente_form['password']):
    print("Non esiste l'utente")
    return redirect(url_for('index'))
  else:
    new = User(id=utente_db['id'], nome=utente_db['nome'] , cognome=utente_db['cognome'], email = utente_db['email'], password=utente_db['password'])
    login_user(new, True)
    print('Success!')

    return redirect(url_for('index'))

@app.route('/recensioni/new', methods=['POST'])
@login_required
def add_recensione():

  recensione = request.form.to_dict()

  if recensione ['recensione'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('index'))

  foto = request.files['imgRecensione']
  if foto.filename != '':
    foto.save('static/'+foto.filename)
    recensione['url_foto'] = foto.filename

  rec = {'testo_recensione': 'test', 'url_foto': 'test_url', 'valutazione': 4, 'piatto': 1}
  piatti_dao.add_recensione(rec)

  return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    db_user = utenti_dao.get_user_by_id(user_id)

    #creo un istanza di user: modello definito in models: richiesto per sapere come gestire l'utente
    user = User(id=db_user['id'], nome = db_user['nome'], cognome = db_user['cognome'], email = db_user['email'], password= db_user['password'])

    return user

@app.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('index'))