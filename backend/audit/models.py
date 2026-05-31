from sqlalchemy import Column
from sqlalchemy import String

from backend.database.db import Base


class AuditLog(Base):

    __tablename__ = "audit_logs"

    event_id = Column(
        String,
        primary_key=True,
        index=True
    )

    agent_id = Column(
        String,
        nullable=False
    )

    action = Column(
        String,
        nullable=False
    )

    status = Column(
        String,
        nullable=False
    )

    timestamp = Column(
        String,
        nullable=False
    )