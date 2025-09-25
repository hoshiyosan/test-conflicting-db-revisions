from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Table, Integer, String, ForeignKey, Column

class DBModel(DeclarativeBase): ...


class DBUser(DBModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
