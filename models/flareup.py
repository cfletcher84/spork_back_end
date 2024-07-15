from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
import datetime

class FlareUp(Base):
    __tablename__ = "flares"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(db.ForeignKey('users.id'), nullable=False)
    flare: Mapped[bool] = mapped_column(db.Boolean)
    # date: Mapped[datetime.date] = mapped_column(db.Date, nullable=False, default=lambda : datetime.datetime.date(datetime.datetime.now()))