from app.main import bp
from flask import render_template, current_app, redirect, url_for, request, flash, redirect, url_for, jsonify
from app import db
from app.mmodels import Case
import cx_Oracle


@bp.route('/', methods=['GET','POST'])
@bp.route('/index/', methods=['GET','POST'])
def index():
    return render_template('apitry.html', title='api1')


@bp.route('/endex/', methods=['GET','POST'])
def endex():
    db.create_all()
    case = Case(casename='loflff22123o2233l')
    db.session.add(case)
    db.session.commit()
    flash('Congratulations, you are now a registered user')
    return redirect(url_for('main.index'))


@bp.route('/cndex/', methods=['GET','POST'])
def cndex():
    connection = cx_Oracle.Connection("hos/hos@192.168.15.50:1521/payy")
    cursor = connection.cursor()
    try:
        cursor.execute("select * from wx_register")
# except cx_Oracle.DatabaseError as exc:
    except Exception as err:
        print("Whoops!")
        print(err)
# print(cursor.description)
    cursor.execute("select id,idcard from wx_register")
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args:dict(zip(columns, args))
    data = cursor.fetchall()
    return render_template('echart.html',title='eeew')

@bp.route('/echarm/', methods=['GET','POST'])
def ech():
    return render_template('apitry.html', title='api1')

@bp.route('/exce/', methods=['GET', 'POST'])
def exce():
    connection = cx_Oracle.Connection("hos/hos@192.168.15.50:1521/payy")
    cursor = connection.cursor()
    try:
        cursor.execute("select * from wx_register")
# except cx_Oracle.DatabaseError as exc:
    except Exception as err:
        print("Whoops!")
        print(err)
# print(cursor.description)
    #cursor.execute("select id,idcard from wx_register")
    #columns = [col[0] for col in cursor.description]
    #cursor.rowfactory = lambda *args:dict(zip(columns, args))
    data = cursor.fetchall()
    return render_template('exce.html', data=data)


@bp.route('/excet/', methods=['GET', 'POST'])
def excet():
    connection = cx_Oracle.Connection("hos/hos@192.168.15.50:1521/payy")
    cursor = connection.cursor()
    try:
        cursor.execute("select * from wx_register")
# except cx_Oracle.DatabaseError as exc:
    except Exception as err:
        print("Whoops!")
        print(err)
# print(cursor.description)
    #cursor.execute("select id,idcard from wx_register")
    #columns = [col[0] for col in cursor.description]
    #cursor.rowfactory = lambda *args:dict(zip(columns, args))
    data = cursor.fetchall()
    return render_template('excet.html', data=data)