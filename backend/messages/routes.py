from fastapi import APIRouter, HTTPException

from backend.messages.schemas import (
    SignRequest,
    VerifyRequest
)

from backend.crypto.signing import (
    sign_message,
    verify_message
)

from backend.agents.routes import AGENTS

router = APIRouter()


@router.post("/messages/sign")
def sign(payload: SignRequest):

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

    signature = sign_message(
        payload.message,
        agent["private_key"]
    )

    return {
        "agent_id": payload.agent_id,
        "message": payload.message,
        "signature": signature
    }


@router.post("/messages/verify")
def verify(payload: VerifyRequest):

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

    result = verify_message(
        payload.message,
        payload.signature,
        agent["public_key"]
    )

    return {
        "verified": result
    }