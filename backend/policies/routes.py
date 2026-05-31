from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import Agent

from backend.policies.schemas import (
    PolicyCheckRequest
)

from backend.policies.policy_engine import (
    is_action_allowed
)

from backend.audit.service import create_audit_event

router = APIRouter()


@router.post("/policies/check")
def check_policy(
    payload: PolicyCheckRequest,
    db: Session = Depends(get_db)
):

    agent = db.query(Agent).filter(
        Agent.agent_id == payload.agent_id
    ).first()

    if not agent:
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )

    allowed = is_action_allowed(
        agent.role,
        payload.action
    )

    create_audit_event(
        db=db,
        agent_id=agent.agent_id,
        action=payload.action,
        status="allowed" if allowed else "denied"
    )

    return {
        "agent_id": agent.agent_id,
        "role": agent.role,
        "action": payload.action,
        "allowed": allowed
    }