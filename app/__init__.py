from flask import Flask
from app.config import Config
from app.extensions import db,migrate,mail
from app.cliente.routes import cliente_api
from app.produtos.routes import produto_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app,db)
    mail.init_app(app)

    app.register_blueprint(cliente_api)
    app.register_blueprint(produto_api)

  
    return app

