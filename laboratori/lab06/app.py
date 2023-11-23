from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {'id': 0,
     'username': 'alberto', 
     'date': '10/11/2023', 
     'text': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam non odio ut elit iaculis laoreet. Fusce sed lacus elementum, accumsan magna non, efficitur neque. Quisque convallis est quis sagittis convallis.', 
     'propic': 'user.jpg', 
     'text': ['''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse aliquet tempor viverra.
                    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
                    egestas. Pellentesque egestas, libero vel convallis efficitur, mauris elit ultricies sem,
                    sed faucibus orci diam id justo. Maecenas finibus viverra ante, vitae placerat ex efficitur
                    vel. Nunc imperdiet aliquet tellus, id consequat sem accumsan a. Pellentesque hendrerit
                    aliquam ante eu commodo. Maecenas lacinia rutrum velit, eu viverra lorem condimentum quis.''',
                '''Proin eu augue sagittis, rhoncus lorem in, viverra ipsum. Aenean sollicitudin eleifend nunc
                    sit amet euismod. Proin scelerisque commodo imperdiet. Suspendisse ac nibh rutrum, fermentum
                    diam viverra, elementum purus. Quisque nec malesuada nibh, non egestas felis. Donec
                    consectetur luctus turpis, semper condimentum urna dictum ut. Donec vitae hendrerit erat.
                    Donec venenatis sem vel lorem hendrerit lobortis. Cras pellentesque ex vitae mauris cursus,
                    nec rutrum velit condimentum. Cras mattis, urna vitae suscipit accumsan, ipsum elit
                    malesuada mi, congue commodo lorem nulla feugiat est. Integer tincidunt nisi nulla, non
                    vehicula quam lobortis ac. Aliquam vitae ex nisl. Sed volutpat, leo at porttitor
                    sollicitudin, libero quam facilisis lectus, vitae malesuada massa eros consequat arcu. Sed
                    tincidunt justo lacus, sit amet tempus libero venenatis ac.''',
                  '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla.
                    Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci
                    tellus, pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed
                    efficitur. Donec porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi
                    tempus consequat.'''],
     'pic': 'img1.jpg',
     'comments': [
       {'user': '@juan',
        'propic' : 'user.jpg',
        'text': '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla. 
                  Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci tellus, 
                  pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed efficitur. Donec 
                  porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi tempus consequat.'''},
        {'user': '@luigi',
        'propic' : 'user.jpg',
        'text': '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla. 
                  Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci tellus, 
                  pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed efficitur. Donec 
                  porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi tempus consequat.'''}
     ]},
     {'id': 1,
     'username': 'luigi', 
     'date': '13/11/2023', 
     'text': ['''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse aliquet tempor viverra.
                    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
                    egestas. Pellentesque egestas, libero vel convallis efficitur, mauris elit ultricies sem,
                    sed faucibus orci diam id justo. Maecenas finibus viverra ante, vitae placerat ex efficitur
                    vel. Nunc imperdiet aliquet tellus, id consequat sem accumsan a. Pellentesque hendrerit
                    aliquam ante eu commodo. Maecenas lacinia rutrum velit, eu viverra lorem condimentum quis.''',
                '''Proin eu augue sagittis, rhoncus lorem in, viverra ipsum. Aenean sollicitudin eleifend nunc
                    sit amet euismod. Proin scelerisque commodo imperdiet. Suspendisse ac nibh rutrum, fermentum
                    diam viverra, elementum purus. Quisque nec malesuada nibh, non egestas felis. Donec
                    consectetur luctus turpis, semper condimentum urna dictum ut. Donec vitae hendrerit erat.
                    Donec venenatis sem vel lorem hendrerit lobortis. Cras pellentesque ex vitae mauris cursus,
                    nec rutrum velit condimentum. Cras mattis, urna vitae suscipit accumsan, ipsum elit
                    malesuada mi, congue commodo lorem nulla feugiat est. Integer tincidunt nisi nulla, non
                    vehicula quam lobortis ac. Aliquam vitae ex nisl. Sed volutpat, leo at porttitor
                    sollicitudin, libero quam facilisis lectus, vitae malesuada massa eros consequat arcu. Sed
                    tincidunt justo lacus, sit amet tempus libero venenatis ac.''',
                  '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla.
                    Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci
                    tellus, pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed
                    efficitur. Donec porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi
                    tempus consequat.'''], 
     'propic': 'user.jpg', 
     'pic': 'img2.jpg',
     'comments': [
       {'user': '@juan',
        'propic' : 'user.jpg',
        'text': '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla. 
                  Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci tellus, 
                  pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed efficitur. Donec 
                  porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi tempus consequat.'''},
        {'user': '@luigi',
        'propic' : 'user.jpg',
        'text': '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla. 
                  Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci tellus, 
                  pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed efficitur. Donec 
                  porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi tempus consequat.'''}
     ]},
     {'id': 2,
     'username': 'juan', 
     'date': '07/11/2023', 
     'text': ['''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse aliquet tempor viverra.
                    Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis
                    egestas. Pellentesque egestas, libero vel convallis efficitur, mauris elit ultricies sem,
                    sed faucibus orci diam id justo. Maecenas finibus viverra ante, vitae placerat ex efficitur
                    vel. Nunc imperdiet aliquet tellus, id consequat sem accumsan a. Pellentesque hendrerit
                    aliquam ante eu commodo. Maecenas lacinia rutrum velit, eu viverra lorem condimentum quis.''',
                '''Proin eu augue sagittis, rhoncus lorem in, viverra ipsum. Aenean sollicitudin eleifend nunc
                    sit amet euismod. Proin scelerisque commodo imperdiet. Suspendisse ac nibh rutrum, fermentum
                    diam viverra, elementum purus. Quisque nec malesuada nibh, non egestas felis. Donec
                    consectetur luctus turpis, semper condimentum urna dictum ut. Donec vitae hendrerit erat.
                    Donec venenatis sem vel lorem hendrerit lobortis. Cras pellentesque ex vitae mauris cursus,
                    nec rutrum velit condimentum. Cras mattis, urna vitae suscipit accumsan, ipsum elit
                    malesuada mi, congue commodo lorem nulla feugiat est. Integer tincidunt nisi nulla, non
                    vehicula quam lobortis ac. Aliquam vitae ex nisl. Sed volutpat, leo at porttitor
                    sollicitudin, libero quam facilisis lectus, vitae malesuada massa eros consequat arcu. Sed
                    tincidunt justo lacus, sit amet tempus libero venenatis ac.''',
                  '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla.
                    Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci
                    tellus, pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed
                    efficitur. Donec porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi
                    tempus consequat.'''], 
     'propic': 'user.jpg', 
     'pic': 'img3.jpg',
     'comments': [
       {'user': '@juan',
        'propic' : 'user.jpg',
        'text': '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla. 
                  Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci tellus, 
                  pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed efficitur. Donec 
                  porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi tempus consequat.'''},
        {'user': '@luigi',
        'propic' : 'user.jpg',
        'text': '''Aliquam imperdiet odio at massa dictum, nec consequat mi fermentum. Mauris a euismod nulla. 
                  Nunc tristique in orci ut finibus. Duis vel est sit amet metus finibus sagittis. In orci tellus, 
                  pretium vitae volutpat in, auctor sagittis est. Donec faucibus vel massa sed efficitur. Donec 
                  porttitor risus eget massa porta scelerisque. Mauris ac ex suscipit nisi tempus consequat.'''}
     ]}
  ]

@app.route('/')
def home():
  # posts list: post content
  # username; 
  # data di pubblicazione; 
  # testo principale;  
  # Il percorso su disco dell’immagine di profilo; 
  # Il percorso su disco dell’immagine del post, se presente.
  # {'username': , 'date': , 'text': , 'propic': , 'pic': }
  
  return render_template('home.html', post_list = posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/post/<int:id>')
def post_page(id):
  [post] = [d for d in posts if d['id'] == id-1]
  return render_template('post.html', post = post)