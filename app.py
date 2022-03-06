#coding:utf-8
from flask import render_template

from base import create_app

app =create_app('develop')

@app.route('/')
def index():
    return render_template("show_entries.html")


if __name__ == '__main__':
    print(app.url_map)
    app.run(host='0.0.0.0')




# def create_app(config_name):
#  """
#  创建flask对象
#  :param config_name: str :
#  :return:
#  """
#  app = Flask(__name__)
#  # 根据配置模式的名字获取配置参数的类
#  config_class= config_map.get(config_name)
#  app.config.from_object(config_class)
#  return app

# 创建redis连接对象
# redis_store = redis.StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)




