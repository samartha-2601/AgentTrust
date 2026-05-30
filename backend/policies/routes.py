from fastapi import APIRouter, HTTPException

from backend.agents.routes import AGENTS

from backend.policies.schemas import (
    PolicyCheckRequest
)

from backend.policies.policy_engine import (
    is_action_allowed
)

router = APIRouter()


@router.post("/policies/check")
def check_policy(
    payload: PolicyCheckRequest
):

    agent = next(
        (
            a for a in AGENTS
            if a["agent_id"] == payload.agent_id
        ),
        None
    )

    if not agent:

        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )

    allowed = is_action_allowed(
        agent["role"],
        payload.action
    )

    return {
        "agent_id": payload.agent_id,
        "role": agent["role"],
        "action": payload.action,
        "allowed": allowed
    }