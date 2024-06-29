from flask import Flask
from database import db
from schemas import ma

from models.users import Users
from models.tasks import Tasks

def create_app(config_name):
    app = Flask(__name__)

    app.config.from_object(f'config.{config_name}')

    db.init_app(app)
    ma.init_app(app)

    return app

if __name__ == '__main__':
    app = create_app('DevelopmentConfig')

    with app.app_context():
        db.drop_all()
        db.create_all()

    
    app.run(debug=True)

