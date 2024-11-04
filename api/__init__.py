from flask import Flask
from flask_restx import Api
from .views import bookNamespace
from .config import config_dict
from .utils import db
from .model import Books
from flask_migrate import Migrate



def create_app(config = config_dict["prod"]):
    app = Flask(__name__)
    app.config.from_object(config)
    db.init_app(app)
    Migrate(app,db)
    api = Api(app,tittle="Library Book Management System",
		  description="A REST API for library management system " )
    api.add_namespace(bookNamespace, path="/api/v1")


    @app.shell_context_processor
    def make_shell_context():
        return {
            "db":db,
            "books":Books,
        }

    return app
    
