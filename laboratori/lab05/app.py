from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
  # posts list: post content
  # username; 
  # data di pubblicazione; 
  # testo principale;  
  # Il percorso su disco dell’immagine di profilo; 
  # Il percorso su disco dell’immagine del post, se presente.
  # {'username': , 'date': , 'text': , 'propic': , 'pic': }
  posts = [
    {'username': 'alberto', 
     'date': '10/11/2023', 
     'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non odio ut elit iaculis laoreet. Fusce sed lacus elementum, accumsan magna non, efficitur neque. Quisque convallis est quis sagittis convallis.', 
     'propic': 'user.jpg', 
     'pic': 'img1.jpg'},
     {'username': 'luigi', 
     'date': '13/11/2023', 
     'text': 'Etiam non odio ut elit iaculis laoreet. Fusce sed lacus elementum, accumsan magna non, efficitur neque. Quisque convallis est quis sagittis convallis. Lorem ipsum dolor sit amet, consectetur adipiscing elit. ', 
     'propic': 'user.jpg', 
     'pic': 'img2.jpg'},
     {'username': 'juan', 
     'date': '07/11/2023', 
     'text': 'Fusce sed lacus elementum, accumsan magna non, efficitur neque. Quisque convallis est quis sagittis convallis.', 
     'propic': 'user.jpg', 
     'pic': 'img3.jpg'}
  ]
  return render_template('home.html', post_list = posts)

@app.route('/about')
def about():
  return render_template('about.html')