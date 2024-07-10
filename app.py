from flask import Flask
from database import db, migrate
from schemas import ma

from models.user import User
from models.task import Task
from models.flareup import FlareUp

from routes.userBP import user_blueprint
from routes.taskBP import task_blueprint
from routes.flareupBP import flare_blueprint

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)

    return app

def blueprint_config(app):
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(task_blueprint, url_prefix='/tasks')
    app.register_blueprint(flare_blueprint, url_prefix='/flareups')

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)
    
    app.run(debug=True)

