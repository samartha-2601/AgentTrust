from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Boolean

from backend.database.db import Base


class TrustChain(Base):

    __tablename__ = "trust_chains"

    chain_id = Column(
        String,
        primary_key=True,
        index=True
    )

    finding = Column(
        String,
        nullable=False
    )

    research_agent = Column(
        String,
        nullable=False
    )

    review_agent = Column(
        String,
        nullable=False
    )

    security_agent = Column(
        String,
        nullable=False
    )

    chain_valid = Column(
        Boolean,
        nullable=False
    )

    timestamp = Column(
        String,
        nullable=False
    )