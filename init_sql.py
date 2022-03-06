# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from base.api_v1.sql import init_db

init_db()

# app=Flask(__name__)
# app.secret_key = os.urandom(24)
#
#
#
#
# @app.route('/')
# def inedx():
#     if 'username' in session:
#         return 'Logged in as %s ' % escape(session['username'])
#     return 'you are not logged in'
#
# @app.route('/login',methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         session['username'] = request.form['username']
#         return redirect(url_for('inedx'))
#     return '''
#         <form action="" method="post">
#             <p><input type=text name=username>
#             <p><input type=submit value=Login>
#         </form>
#     '''
# @app.route('/logout')
# def logout():
#     session.pop('username',None)
#     return  redirect(url_for('inedx'))


# @app.route('/')
# @app.route('/<name>')
# def print_hi(name=None):
#     # 在下面的代码行中使用断点来调试脚本。
#     # return  render_template('hello.html',name=name)     # 按 Ctrl+F8 切换断点。
#     return redirect(url_for('login'))
#
#
# @app.route('/login' ,methods=['GET','POST'])
# def login():
#     if request.method=='POST':
#         return  do_the_login()
#     else:
#         return show_the_login_form()
#
# @app.route('/with/')
# def wu():
#     return 'with'
#
# @app.route('/without')
# def you():
#     return 'without'
#
#
# def do_the_login():
#     pass
#
# def show_the_login_form():pass
#
#
#
# with app.test_request_context():
#     print(url_for('print_hi',name='xct'))

# 按间距中的绿色按钮以运行脚本。


# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助
