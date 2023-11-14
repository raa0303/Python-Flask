from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "b'\x1a(\xe4\x9bu3\x02\x13\xd9\xa2;\xd5\xd8\xe1@\x93'"