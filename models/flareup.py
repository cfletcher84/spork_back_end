from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column

class FlareUp(Base):
    __tablename__ = "flares"
    id: Mapped[int] = mapped_column(primary_key=True)
    flare: Mapped[bool] = mapped_column(db.Boolean)
    date: Mapped[str] = mapped_column(db.String(100))