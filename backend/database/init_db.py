from backend.database.db import engine, Base

from backend.database.models import Agent


def create_tables():

    Base.metadata.create_all(bind=engine)