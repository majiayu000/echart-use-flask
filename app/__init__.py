from flask import Flask, current_app, request
from config import Config
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_moment import Moment
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_bootstrap import Bootstrap


db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
moment = Moment()
bootstrap = Bootstrap()

def after_request(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT,GET,POST,DELETE'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response

# app的配置  chj：账号  123456：密码   ORCL：链接的数据库
# app.config['SQLALCHEMY_DATABASE_URI'] = 'oracle://chj:123456@127.0.0.1:1521/ORCL'

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.after_request(after_request)

    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)


    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    from app.api_1_0 import bp as api_bp
    app.register_blueprint(api_bp)

    if not app.debug and not app.testing:
        if app.config['MAIL_SERVER']:
            auth = None
            if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
                auth = (app.config['MAIL_USERNAME'],
                        app.config['MAIL_PASSWORD'])
            secure = None
            if app.config['MAIL_USE_TLS']:
                secure=()
            mail_handle = SMTPHandler(
                mailhost=(app.config['MAIL_SERVER'],app.config['MAIL_PORT']),
                fromaddr='no_reply@' + app.config['MAIL_SERVER'],
                toaddrs=app.config['ADMINS'],
                subject='系统错误',
                credentials=auth,
                secure=secure
            )
            mail_handle.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handle)
    return app