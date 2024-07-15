from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(300), unique=True)
    password: Mapped[str] = mapped_column(db.String(500), nullable=False)
    spoons: Mapped[int] = mapped_column(nullable=False)
    profile_pic: Mapped[str] = mapped_column(db.String(100), nullable=True)
    task: Mapped['Task'] = db.relationship(back_populates='user')