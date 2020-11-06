from app.api_1_0 import bp
from flask import render_template, current_app, redirect, url_for, request, flash, redirect, url_for, jsonify
from app import db
from app.mmodels import Case
import cx_Oracle


@bp.route('/getuser/', methods=['GET'])
def userrequest():
    connection = cx_Oracle.Connection("hos/hos@192.168.15.50:1521/payy")
    cursor = connection.cursor()
    try:
        cursor.execute("select * from wx_register")
    except Exception as err:
        print("Whoops!")
        print(err)
    cursor.execute("select id,address from wx_register")
    columns = [col[0] for col in cursor.description]
    cursor.rowfactory = lambda *args:dict(zip(columns, args))
    data = cursor.fetchall()
    return jsonify({'list': data})
   