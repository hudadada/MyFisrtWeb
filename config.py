from datetime import timedelta

import logging
from redis import StrictRedis


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

class Development(Config):
    DEBUG = True
    LOG_LEVEL = logging.DEBUG

class Production(Config):
    DEBUG = False
    LOG_LEVEL = logging.ERROR


config_dict = {
    "dev":Development,
    "pro":Production

}


