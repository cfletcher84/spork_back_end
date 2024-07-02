from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    email: Mapped[str] = mapped_column(db.String(300), unique=True)
    password: Mapped[str] = mapped_column(db.String(50), nullable=False)
    spoons: Mapped[int] = mapped_column(nullable=False)
    spoons_used: Mapped[int] = mapped_column(nullable=False)
    # task: Mapped['Task'] = db.relationship(back_populates='users')