from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Table, Integer, String, ForeignKey, Column

class DBModel(DeclarativeBase): ...


class DBUser(DBModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)


class Group(DBModel):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)


user_groups = Table(
    "user_groups", DBModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("group_id", ForeignKey("groups.id"), primary_key=True)
)
