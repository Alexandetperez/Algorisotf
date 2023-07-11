import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQLITE={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db/sqlite/db.sqlite3')
    }
}
MYSQL = {
  'default':{
  'ENGINE':'django.db.backends.mysql',
  'NAME':'Algorisotf', #nombre de la base de datos
  'USER':'Alexander',
  'PASSWORD':'18Sep.1998',
  'HOST':'20.120.35.24', #servidor local o también puede ser 'localhost'
  'PORT':'3306'
  }
}
