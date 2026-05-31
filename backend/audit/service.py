import uuid

from datetime import datetime

from backend.audit.models import AuditLog


def create_audit_event(
    db,
    agent_id,
    action,
    status
):

    event = AuditLog(
        event_id=str(uuid.uuid4()),
        agent_id=agent_id,
        action=action,
        status=status,
        timestamp=datetime.utcnow().isoformat()
    )

    db.add(event)

    db.commit()

    db.refresh(event)

    return event