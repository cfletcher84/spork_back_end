from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db, Base
import datetime

class Task(Base):
    __tablename__ = 'tasks'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    task: Mapped[str] = mapped_column(db.String(255))
    description: Mapped[str] = mapped_column(db.String(500))
    date: Mapped[str] = mapped_column(db.String(20), nullable=True)
    spoons_needed: Mapped[int] = mapped_column(db.Integer())
    duration: Mapped[str] = mapped_column(db.String(100))
    time_of_day: Mapped[str] = mapped_column(db.String(100))
    icon: Mapped[str] = mapped_column(db.String(500), nullable=True)
    user: Mapped['User'] = relationship('User', back_populates='tasks') 

from models.user import User
