import redis

class Config(object):
    PASSWORD = 'admin'
    USERNAME = 'admin'
    DATABASE = 'J:/python/flaskr/base/data/flaskr.db'
    SECRET_KEY = 'SECRET_KEY'
    REDIS_HOST= "127.0.0.1"
    REDIS_PORT = 6379

    # falsk_session的配置
    SESSION_TYPE = "redis"
    SESSION_REDIS = redis.StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    SESSION_USER_SIGNER = True      #对cookoe中的session_id进行隐藏
    PRERMANECND_SESSION_LIFETIME = 43200        #session数据的有效期 单位 秒

class DevelopmentConfig(Config):
    pass
    # DEBUG =True
class ProductionConfig(Config):
    pass

config_map = {
    "develop": DevelopmentConfig,
    "product": ProductionConfig
}

