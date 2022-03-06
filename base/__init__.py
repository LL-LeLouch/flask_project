# coding:utf-8
from flask import Flask, g

from base import api_v1
from config import config_map

# 创建redis连接对象
redis_store = None


def create_app(config_name):
    """
    创建flask对象
    :param config_name: str :
    :return:
    """


    app = Flask(__name__)
    # 根据配置模式的名字获取配置参数的类
    config_class= config_map.get(config_name)
    app.config.from_object(config_class)



    #初始化redis工具
    # global redis_store
    # redis_store = redis.StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)


    # 利用flask-session 将session数据保存在redis中
    # Session(app)

    # 为flask补充csrf防护
    # CSRFProtect(app)


    #注册蓝图
    app.register_blueprint(api_v1.api,url_prefix="/api/v1")

    # 断开连接
    @app.teardown_appcontext
    def close_db(error):
        if hasattr(g, 'sqlite_db'):
            g.sqlite_db.close()

    return app