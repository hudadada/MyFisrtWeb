from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

app = Flask(__name__)

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/myfirstweb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

app.config.from_object(Config)
db = SQLAlchemy(app)
sr = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)

@app.route('/')
def index():

    return 'index is show'

if __name__ == '__main__':
    app.run()