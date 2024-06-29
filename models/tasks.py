from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Tasks(Base):
    __tablename__ = 'Tasks'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('Users.id'))
    task: Mapped[str] = mapped_column(db.String(255))
    description: Mapped[str] = mapped_column(db.String(500))
    date: Mapped[str] = mapped_column(db.String(200))
    spoons_needed: Mapped[int] = mapped_column(db.Integer())
    user: Mapped['Users'] = db.relationship(back_populates='tasks')