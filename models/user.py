from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db, Base

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(300), unique=True)
    password: Mapped[str] = mapped_column(db.String(500), nullable=False)
    # spoons: Mapped[int] = mapped_column(nullable=False, default=12)
    profile_pic: Mapped[str] = mapped_column(db.String(100), nullable=True)
    tasks: Mapped[list['Task']] = relationship('Task', back_populates='user')
    spoons: Mapped['Spoons'] = relationship('Spoons', back_populates='user')
    
from models.task import Task
from models.spoons import Spoons
