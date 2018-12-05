from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

app = Flask(__name__)

class Config:
    # 调试模式开启
    DEBUG = True
    # mysql数据库
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/myfirstweb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # REDIS数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    # 配置session 存储
    SESSION_TYPE = 'redis'
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USER_SIGNER = True
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
#封装配置 从对象中加载配置
app.config.from_object(Config)
#创建数据库连接对象
db = SQLAlchemy(app)
# 创建redis连接对象
sr = StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 初始化session存储对象
Session(app)
# 创建脚本启动管理器
mgr = Manager(app)
#初始化迁移器
Migrate(app,db)
# 生成迁移命令
mgr.add_command("mc",MigrateCommand)

@app.route('/')
def index():

    return 'index is show'

if __name__ == '__main__':
    mgr.run()