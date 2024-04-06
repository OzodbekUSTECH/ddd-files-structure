from app.infrastucture.db.models import Base
from sqlalchemy.orm import Mapped


class File(Base):
    __tablename__ = "files"

    name: Mapped[str]
    path: Mapped[str]
