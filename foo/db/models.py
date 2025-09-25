from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy import Enum as SQLEnum, Table, Integer, String, ForeignKey, Column
from enum import Enum

class DBModel(DeclarativeBase): ...


class DBUser(DBModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)


class DBRole(DBModel):
    __tablename__ = "roles"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    code: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)
    description: Mapped[str] = mapped_column(String(150), nullable=True)


users_roles = Table(
    "users_roles", DBModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("role_id", ForeignKey("roles.id"), primary_key=True)
)


class Group(DBModel):
    __tablename__ = "groups"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True, nullable=False)


user_groups = Table(
    "user_groups", DBModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("group_id", ForeignKey("groups.id"), primary_key=True)
)


class UserFriendShipState(Enum):
    ignored = "ignored"
    denied = "denied"
    requested = "requested"
    pending = "pending"
    accepted = "accepted"


users_friendships = Table(
    "users_friendships", DBModel.metadata,
    Column("user_id", ForeignKey("users.id"), primary_key=True),
    Column("friend_id", ForeignKey("users.id"), primary_key=True),
    Column("state", SQLEnum(UserFriendShipState), nullable=False),
)
