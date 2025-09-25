from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from foo.db.models import DBModel

database_url = "sqlite:///db.sqlite"
engine = create_engine(database_url)
session = scoped_session(sessionmaker(bind=engine))
