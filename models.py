import json
from typing import Optional
from sqlalchemy.dialects.postgresql import JSONB
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
)


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class FormData(Base):
    __tablename__ = "form_data"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[Optional[dict]] = mapped_column(JSONB)

    def __repr__(self):
        return json.dumps(self.data)
