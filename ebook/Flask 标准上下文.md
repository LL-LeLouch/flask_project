下面的全局变量默认在 Jinja2 模板中可用:

config 当前的配置对象 (flask.config)

0.6 新版功能.

在 0.10 版更改: 现在这总是可用的，甚至在导入的模版里。

request 当前的请求对象 (flask.request)。当模版不是在活动的请求上下 文中渲染时这个变量不可用。

session 当前的会话对象 (flask.session)。当模版不是在活动的请求上下 文中渲染时这个变量不可用。

g 请求相关的全局变量 (flask.g)。当模版不是在活动的请求上下 文中渲染时这个变量不可用。

url_for()
flask.url_for() 函数

get_flashed_messages()
flask.get_flashed_messages() 函数

Jinja 上下文行为

这些变量被添加到了请求的上下文中，而非全局变量。区别在于，他们默认不会 在导入模板的上下文中出现。这样做，一方面是考虑到性能，另一方面是为了 让事情显式透明。

这对你来说意味着什么？如果你想要导入一个需要访问请求对象的宏，有两种可能的方法:

显式地传入请求或请求对象的属性作为宏的参数。 与上下文一起（with context）导入宏。 与上下文中一起（with context）导入的方式如下:

{% from '_helpers.html' import my_macro with context %}