from flask import Flask
from database import db, migrate
from schemas import ma
from dotenv import load_dotenv
from flask_cors import CORS

from models.user import User
from models.task import Task
from models.flareup import FlareUp

from routes.userBP import user_blueprint
from routes.taskBP import task_blueprint
from routes.flareupBP import flare_blueprint
from routes.tokenBP import token_blueprint
from routes.spoonsBP import spoons_blueprint

load_dotenv()

def create_app(config_name):
    app = Flask(__name__)
    cors = CORS(app)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    blueprint_config(app)

    return app

def blueprint_config(app):
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(task_blueprint, url_prefix='/tasks')
    app.register_blueprint(flare_blueprint, url_prefix='/flareups')
    app.register_blueprint(token_blueprint, url_prefix='/token')
    app.register_blueprint(spoons_blueprint, url_prefix='/spoons')

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')
    
    app.run(debug=True)

