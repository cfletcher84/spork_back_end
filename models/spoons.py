from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import db, Base

class Spoons(Base):
    __tablename__ = "spoons"
    id: Mapped[int] = mapped_column(primary_key=True)
    spoons: Mapped[int] = mapped_column(nullable=False, default=12)
    date: Mapped[str] = mapped_column(db.String(20), nullable=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    user: Mapped['User'] = relationship('Spoons', back_populates='user') 

    
from models.user import User
