from fastapi import APIRouter, HTTPException, Depends

from sqlalchemy.orm import Session

from backend.messages.schemas import (
    SignRequest,
    VerifyRequest
)

from backend.crypto.signing import (
    sign_message,
    verify_message
)

from backend.database.dependencies import get_db
from backend.database.models import Agent

router = APIRouter()


@router.post("/messages/sign")
def sign(
    payload: SignRequest,
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

    signature = sign_message(
        payload.message,
        agent.private_key
    )

    return {
        "agent_id": agent.agent_id,
        "message": payload.message,
        "signature": signature
    }


@router.post("/messages/verify")
def verify(
    payload: VerifyRequest,
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

    verified = verify_message(
        payload.message,
        payload.signature,
        agent.public_key
    )

    return {
        "verified": verified
    }