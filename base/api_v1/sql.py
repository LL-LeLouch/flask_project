import sqlite3

from flask import render_template, abort, flash, request, redirect, session, url_for, g

from config import Config
from . import api


# 初始化数据库
def init_db():
    # with closing(connect_db()) as db:
    with api.app_context():
        db = get_db()
        with api.open_resource('schema.data', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# 连接sqllte3
def connect_db():
    rv = sqlite3.connect(Config.DATABASE)
    return rv

# 将sqlite3连接放到g.sqlite_db
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


# 显示条目
@api.route('/')
def show_entries():
    if session.get('logged_in'):
        g.db = connect_db()
        cur = g.db.execute('select title, text , id from entries order by id desc')
        entries = [dict(id=row[0], title=row[1], text=row[2]) for row in cur.fetchall()]
        return render_template('show_entries.html', entries=entries)
    else:
        return render_template('show_entries.html')



# 添加条目
@api.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db = connect_db()
    g.db.execute('insert into entries (title,text) values (?,?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successful posted')
    return redirect(url_for('show_entries'))


@api.route('/del', methods=['POST'])
def del_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db = connect_db()
    g.db.execute('delete from entries where id = ?  ',
                 [request.form['ID']])
    g.db.commit()
    flash('del entry was successful')
    return redirect(url_for('show_entries'))