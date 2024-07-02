from flask import Flask
from database import db
from schemas import ma

from models.user import User
from models.task import Task

from routes.userBP import user_blueprint
from routes.taskBP import task_blueprint

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)

    return app

def blueprint_config(app):
    app.register_blueprint(user_blueprint, url_prefix='/users')
    app.register_blueprint(task_blueprint, url_prefix='/tasks')

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    blueprint_config(app)

    with app.app_context():
        db.drop_all()
        db.create_all()

    
    app.run(debug=True)

