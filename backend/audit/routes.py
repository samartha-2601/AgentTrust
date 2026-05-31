from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db

from backend.audit.models import AuditLog

router = APIRouter()


@router.get("/audit/logs")
def get_logs(
    db: Session = Depends(get_db)
):

    logs = db.query(AuditLog).all()

    return [
        {
            "event_id": log.event_id,
            "agent_id": log.agent_id,
            "action": log.action,
            "status": log.status,
            "timestamp": log.timestamp
        }
        for log in logs
    ]