from sqlalchemy.orm import Mapped

from app.infrastructure.db.models import Base


class File(Base):
    __tablename__ = "files"

    name: Mapped[str]
    path: Mapped[str]
