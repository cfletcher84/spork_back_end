from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
import datetime
from models.user import User
class FlareUp(Base):
    __tablename__ = "flares"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    flare: Mapped[bool] = mapped_column(db.Boolean)
    date: Mapped[str] = mapped_column(db.String(20), nullable=True)
    # user: Mapped['User'] = relationship('User', back_populates='flares')