如果你要在 Jinja2 中注册你自己的过滤器，你有两种方法。你可以把它们手动添加到 应用的 jinja_env 或者使用 template_filter() 装饰器。

下面两个例子作用相同，都是反转一个对象:

@app.template_filter('reverse')
def reverse_filter(s):
return s[::-1]

def reverse_filter(s):
return s[::-1]
app.jinja_env.filters['reverse'] = reverse_filter 在使用装饰器的情况下，如果你想以函数名作为过滤器名，参数是可选的。注册之后， 你可以在模板中像使用 Jinja2
内置过滤器一样使用你的过滤器，例如你在上下文中有 一个名为 mylist 的 Python 列表:

{% for x in mylist | reverse %} {% endfor %}