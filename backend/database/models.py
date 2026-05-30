from sqlalchemy import Column, String

from backend.database.db import Base


class Agent(Base):

    __tablename__ = "agents"

    agent_id = Column(
        String,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    role = Column(
        String,
        nullable=False
    )

    public_key = Column(
        String,
        nullable=False
    )

    private_key = Column(
        String,
        nullable=False
    )