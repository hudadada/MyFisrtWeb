from flask import Flask
from flask_migrate import Migrate

from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis

from config import config_dict



def create_app(config_type):
    config_class = config_dict.get(config_type)
    app = Flask(__name__)
    # 封装配置 从对象中加载配置
    app.config.from_object(config_class)
    # 创建数据库连接对象
    db = SQLAlchemy(app)
    # 创建redis连接对象
    sr = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    # 初始化session存储对象
    Session(app)

    # 初始化迁移器
    Migrate(app, db)

    from info.modules.home import home_blue
    app.register_blueprint(home_blue)

    return app

