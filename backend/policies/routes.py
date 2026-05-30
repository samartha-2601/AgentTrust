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

    return {
        "agent_id": agent.agent_id,
        "role": agent.role,
        "action": payload.action,
        "allowed": allowed
    }