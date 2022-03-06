Flask 订阅信号
2021-08-10 17:49 更新
你可以使用信号的 connect() 方法来订阅信号。该 函数的第一个参数是信号发出时要调用的函数，第二个参数是可选的，用于确定信号 的发送端。退订一个信号，可以使用 disconnect() 方法。

对于所有的核心 Flask 信号，发送端都是发出信号的应用。当你订阅一个信号，请 确保也提供一个发送端，除非你确实想监听全部应用的信号。这在你开发一个扩展 的时候尤其正确。

比如这里有一个用于在单元测试中找出哪个模板被渲染和传入模板的变量的助手上 下文管理器:

from flask import template_rendered
from contextlib import contextmanager

@contextmanager
def captured_templates(app):
    recorded = []
    def record(sender, template, context, **extra):
        recorded.append((template, context))
    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
这可以很容易地与一个测试客户端配对:

with captured_templates(app) as templates:
    rv = app.test_client().get('/')
    assert rv.status_code == 200
    assert len(templates) == 1
    template, context = templates[0]
    assert template.name == 'index.html'
    assert len(context['items']) == 10
确保订阅使用了一个额外的 **extra 参数，这样当 Flask 对信号引入新参数 时你的调用不会失败。

代码中，从 with 块的应用 app 中流出的渲染的所有模板现在会被记录到 templates 变量。无论何时模板被渲染，模板对象和上下文中都会被添加到它 里面。

此外，也有一个方便的助手方法（ connected_to() ） ，它允许你临时地把函数订阅到信号并使用信号自己的上下文管理器。因为这个上下文 管理器的返回值不能由我们决定，所以必须把列表作为参数传入:

from flask import template_rendered

def captured_templates(app, recorded, **extra):
    def record(sender, template, context):
        recorded.append((template, context))
    return template_rendered.connected_to(record, app)
上面的例子会看起来是这样:

templates = []
with captured_templates(app, templates, **extra):
    ...
    template, context = templates[0]
Blinker API 变更

connected_to() 方法出现于 Blinker 1.1 。