import os
import tempfile
import unittest

import flask

import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()
        app.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    # 在 setUp() 方法的代码创建了一个新的测试 客户端并且初始化了一个新的数据库。这个函数将会在每次独立的测试函数 运行之前运行。
    # 要在测试之后删除这个数据库，我们在 tearDown() 函数当中关闭这个文件，并将它从文件系统中删除。
    # 同时，在初始化的时候 TESTING 配置标志被激活，这将会使得处理请求时的错误捕捉失效，以便于 您在进行对应用发出请求的测试时获得更好的错误反馈。
    #
    # 这个测试客户端将会给我们一个通向应用的简单接口，我们可以激发 对向应用发送请求的测试，
    # 并且此客户端也会帮我们记录 Cookie 的 动态。
    #
    # 因为 SQLite3 是基于文件系统的，我们可以很容易的使用临时文件模块来 创建一个临时的数据库并初始化它，
    # 函数 mkstemp() 实际上完成了两件事情：它返回了一个底层的文件指针以及一个随机 的文件名，后者我们用作数据库的名字。
    # 我们只需要将 db_fd 变量 保存起来，就可以使用 os.close 方法来关闭这个文件。

    def test_emty_db(self):
        rv = self.app.get('/')
        assert 'No entries here so far' in str(rv.data)

    # 测试要以test——开头

    # 通过使用 self.app.get 我们可以发送一个 HTTP GET 请求给应用的 某个给定路径。
    # 返回值将会是一个 response_class 对象。我们可以使用 data 属性 来检查程序的返回值(以字符串类型)。
    # 在这里，我们检查 'No entries here so far' 是不是输出内容的一部分。

    def login(self, username, password):
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def test_login_logout(self):
        rv = self.login('admin', 'admin')
        assert 'You were logged in' in str(rv.data)
        rv = self.logout()
        assert 'You were logged out' in str(rv.data)
        rv = self.login('adminx', 'admin')
        assert 'Invalid username' in str(rv.data)
        rv = self.login('admin', 'default')
        assert 'Invalid password' in str(rv.data)

    def test_messages(self):
        self.login('admin', 'admin')
        rv = self.app.post('/add', data=dict(
            title='<Hello>',
            text='<strong>HTML</strong> allowed here'
        ), follow_redirects=True)
        assert 'No entries here so far' not in str(rv.data)
        assert '&lt;Hello&gt;' in str(rv.data)
        assert '<strong>HTML</strong> allowed here' in str(rv.data)


# 有一个 test_request_context() 方法可以 配合 with 语句用于激活一个临时的请求上下文。通过 它，您可以访问 request 、g 和 session 类的对象

app = flask.Flask(__name__)

with app.test_request_context('/?name=Peter'):
    assert flask.request.path == '/'
    assert flask.request.args['name'] == 'Peter'

if __name__ == '__main__':
    unittest.main()
