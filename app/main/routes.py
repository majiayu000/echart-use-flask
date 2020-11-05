from app.main import bp
from flask import current_app, redirect, url_for, request
from app import db
from app.mmodels import Case


@bp.route('/', methods=['GET','POST'])
@bp.route('/index/', methods=['GET','POST'])
def index():
    return 'HELLO'


@bp.route('/endex/', methods=['GET','POST'])
def endex():
    db.create_all()
    case = Case(casename='lolol')
    db.session.add(case)
    db.session.commit()