import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

MIGRATIONS_FOLDER = os.environ.get('MIGRATIONS_FOLDER') or 'migrations'

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class = Base)
migrate = Migrate(directory=MIGRATIONS_FOLDER)

