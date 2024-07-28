from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from models.user import User
from models.task import Task
from models.flareup import FlareUp 
from models.spoons import Spoons