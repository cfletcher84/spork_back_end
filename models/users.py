from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class Users(Base):
    __tablename__ = "Users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(300), unique=True)
    username: Mapped[str] = mapped_column(db.String(300), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(50), nullable=False)
    spoons: Mapped[int] = mapped_column(db.Integer(), nullable=False)
    spoons_used: Mapped[int] = mapped_column(db.Integer(), nullable=False)
    task: Mapped['Tasks'] = db.relationship(back_populates='users')