from flask import Flask, render_template, url_for, redirect, request
from datetime import datetime
import social_dao

app = Flask(__name__)


def get_datetime():
  da_ti = datetime.now()
  (date, time) = str(da_ti).split(' ')
  return date


@app.route('/')
def home():
  posts = social_dao.get_posts()

  users = social_dao.get_users()
  
  return render_template('home.html', post_list = posts, user_list = users, date = get_datetime())


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/post/<int:id>')
def post_page(id):
  post = social_dao.get_single_post(id)
  comments = social_dao.get_post_comments(id)

  return render_template('post.html', post = post, comments = comments)


def validation(post, date):
  valid = True
  if len(post['testo'])<30 or len(post['testo'])>200:
    return False
  postdata = post['data_sort']
  print(postdata, " ", date)
  if postdata < date:
    return False
  return valid

@app.route('/post/new', methods = ['POST'])
def new_post():
  addpost = request.form.to_dict()
  # to get the current date
  (YY, MM, DD) = addpost['data_sort'].split('-')
  data = get_datetime()
  addpost['data_pubblicazione'] = str(DD).rjust(2, '0') +"/"+str(MM).rjust(2,'0')+"/"+str(YY)
  # validation
  if validation(post=addpost, date=data):
    picture = request.files['immagine_post']
    if picture.filename != '':
      picture.save('static/' + picture.filename + addpost['id_utente'])
      addpost['immagine_post'] = picture.filename + addpost['id_utente']
    else:
      addpost['immagine_post'] = ''
    
    done = social_dao.add_post(addpost)
    if (done):
      app.logger.info(addpost)
    else:
      app.logger.error('Error inserting data in the db')
  else:
    app.logger.error('Data inserted not valid')
  return redirect(url_for('home'))


def valid_comment(username, text, evaluation):
  valid = True
  if username != '' and len(username) > 50:
    return False
  if len(text) > 200:
    return False
  if evaluation.isdigit() and int(evaluation) < 1 or int(evaluation) > 5:
    return False
  return valid

@app.route('/comment', methods =['POST'])
def new_comment():
  addcomment = request.form.to_dict()

  addcomment['data_pubblicazione'] = get_datetime()

  addcomment['id_post'] = int(addcomment['id_post'])
  
  has_user = False
  if addcomment['user'] != '':
    has_user = True
    user = social_dao.check_existing_user(addcomment['user'])
    if user == []:
      added_user = social_dao.add_user(addcomment['user'])
      user = social_dao.check_existing_user(addcomment['user'])
    addcomment['id_utente'] = user['id']

  picture = request.files['immagine']
  has_img = False
  if picture.filename != '':
    has_img = True
    picture.save('static/' + picture.filename)
    addcomment['immagine'] = picture.filename
  else:
    addcomment['immagine'] = ''

  done = social_dao.add_comment(addcomment, has_user, has_img)
  if (done):
    app.logger.info(addcomment)
  else:
    app.logger.error('Error inserting data in the db')

  return redirect(url_for('post_page', id=addcomment['id_post']))