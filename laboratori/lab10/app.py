from flask import Flask, render_template, url_for, redirect, request, flash
from datetime import datetime
from flask_login import LoginManager, login_user, login_required, logout_user
from flask_session import Session
from models import User
import utenti_dao, utenti_dao, commenti_dao, posts_dao
from werkzeug.security import generate_password_hash, check_password_hash
import os.path

app = Flask(__name__)

app.config['SECRET_KEY'] = 'valore'

login_manager = LoginManager()
login_manager.init_app(app)


def get_datetime():
  da_ti = datetime.now()
  (date, time) = str(da_ti).split(' ')
  return date


@app.route('/')
def home():
  posts = posts_dao.get_posts()
  users = utenti_dao.get_users()
  
  return render_template('home.html', post_list = posts, user_list = users, date = get_datetime())


@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/iscriviti')
def iscriviti():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup():

  new_user_from_form = request.form.to_dict()

  if new_user_from_form ['nickname'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('home'))
  if new_user_from_form ['password'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('home'))
  
  new_user_from_form ['nickname'] = '@'+new_user_from_form ['nickname']
  new_user_from_form['password'] = generate_password_hash(new_user_from_form['password'])

  picture = request.files['immagine_profilo']
  if picture.filename != '':
    (namefile ,ext)= os.path.splitext(picture.filename)
    if ext != '.jpg' and ext != '.gif' and ext != '.png':
      app.logger.error('Formato del file non supportato')
      return redirect(url_for('home'))
    namefile = namefile + str(datetime.now()) + ext
    picture.save('static/' + namefile)
    new_user_from_form['immagine_profilo'] = namefile
  else:
    new_user_from_form['immagine_profilo'] = None
    
  success = utenti_dao.creare_utente(new_user_from_form)

  if success:
    return redirect(url_for('home'))
  
  return redirect(url_for('iscriviti'))


@app.route('/login', methods=['POST'])
def login():

  utente_form = request.form.to_dict()

  if utente_form ['nickname'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('home'))
  if utente_form ['password'] == '':
    app.logger.error('Il campo non può essere vuoto')
    return redirect(url_for('home'))

  utente_form ['nickname'] = '@'+utente_form ['nickname']
  utente_db = utenti_dao.get_user_by_nickname(utente_form['nickname'])

  if not utente_db:
    flash("Non esiste l'utente")
    return redirect(url_for('home'))
  elif not check_password_hash(utente_db['password'], utente_form['password']):
    flash("Password errata")
    return redirect(url_for('home'))
  else:
    new = User(id=utente_db['id'], nickname=utente_db['nickname'] , password=utente_db['password'], immagine_profilo=utente_db['immagine_profilo'])
    login_user(new, True)
    flash('Success!')

    return redirect(url_for('home'))



@app.route('/post/<int:id>')
def post_page(id):
  post = posts_dao.get_single_post(id)
  comments = commenti_dao.get_post_comments(id)

  return render_template('post.html', post = post, comments = comments)


def validation(post, date):
  valid = True
  if len(post['testo'])<30 or len(post['testo'])>200:
    return False
  if post['data_sort'] < date:
    return False
  return valid

@app.route('/post/new', methods = ['POST'])
@login_required
def new_post():
  addpost = request.form.to_dict()

  # to get the current date
  currentdate = get_datetime()
  if addpost['data_sort'] < currentdate:
    app.logger.error('Not valid date')
    return redirect(url_for('home'))
  if len(addpost['testo'])<30 or len(addpost['testo'])>200:
    app.logger.error('Not valid text')
    return redirect(url_for('home'))
  
  # to format the output date
  (YY, MM, DD) = addpost['data_sort'].split('-')
  addpost['data_pubblicazione'] = str(DD).rjust(2, '0') +"/"+str(MM).rjust(2,'0')+"/"+str(YY)

  picture = request.files['immagine_post']
  if picture.filename != '':
    (name ,ext)= os.path.splitext(picture.filename)
    if ext != '.jpg' and ext != '.gif' and ext != '.png':
      app.logger.error('Formato del file non supportato')
      return redirect(url_for('home'))
    namefile = name + str(datetime.now()) + ext
    picture.save('static/' + namefile)
    addpost['immagine_post'] = namefile
  else:
    addpost['immagine_post'] = None
    
  done = posts_dao.add_post(addpost)
  if (done):
    app.logger.info(addpost)
  else:
    app.logger.error('Error inserting data in the db')
  return redirect(url_for('home'))


@app.route('/comment', methods =['POST'])
@login_required
def new_comment():
  addcomment = request.form.to_dict()

  if len(addcomment['testo']) > 200 or addcomment['testo'] == '':
    app.logger.error('Not valid text')
    return redirect(url_for('home'))
  if not addcomment['valutazione'].isdigit():
    app.logger.error('Evaluation must be an integer number')
    return redirect(url_for('home'))
  if int(addcomment['valutazione']) < 1 or int(addcomment['valutazione']) > 5:
    app.logger.error('Value out of range')
    return redirect(url_for('home'))
  if addcomment['id_post'] == '':
    app.logger.error('Comment must be associated to a post')
    return redirect(url_for('home'))
  
  check_post = posts_dao.check_existing_post(int(addcomment['id_post']))

  if check_post == None or check_post['id'] != int(addcomment['id_post']):
    app.logger.error('Comment must be associated to an existing post')
    return redirect(url_for('home'))

  date = get_datetime()
  addcomment['data_pubblicazione'] = date
  addcomment['id_post'] = int(addcomment['id_post'])
  
  picture = request.files['immagine']
  if picture.filename != '':
    (name ,ext)= os.path.splitext(picture.filename)
    if ext != '.jpg' and ext != '.gif' and ext != '.png':
      app.logger.error('Formato del file non supportato')
      return redirect(url_for('home'))
    namepic = name + str(datetime.now()) + ext
    picture.save('static/' + namepic)
    addcomment['immagine'] = namepic
  else:
    addcomment['immagine'] = None

  print("Id utente: ", addcomment['id_utente'])

  done = commenti_dao.add_comment(addcomment)
  if (done):
    app.logger.info(addcomment)
  else:
    app.logger.error('Error inserting data in the db')

  return redirect(url_for('post_page', id=addcomment['id_post']))


@login_manager.user_loader
def load_user(user_id):
    db_user = utenti_dao.get_user_by_id(user_id)

    #creo un istanza di user: modello definito in models: richiesto per sapere come gestire l'utente
    user = User(id=db_user['id'], nickname = db_user['nickname'], password = db_user['password'], immagine_profilo = db_user['immagine_profilo'])

    return user

@app.route("/logout")
@login_required
def logout():
  logout_user()
  return redirect(url_for('home'))