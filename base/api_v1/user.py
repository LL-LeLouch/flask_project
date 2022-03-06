from flask import request, session, flash, redirect, render_template

from config import Config
from . import api


#登录
@api.route('/login',methods=['POST','GET'])
def login():
    error = None
    if request.method== 'POST':
        if request.form['username'] != Config.USERNAME:
            error = 'Invalid username'
        elif request.form['password'] != Config.PASSWORD:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect('/')
    return render_template('login.html',error=error)

#退出
@api.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect('/')
