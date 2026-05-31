from backend.database.db import engine, Base

from backend.database.models import Agent
from backend.audit.models import AuditLog
from backend.trust_chain.models import TrustChain


def create_tables():

    Base.metadata.create_all(bind=engine)