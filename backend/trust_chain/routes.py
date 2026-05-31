from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from backend.database.dependencies import get_db
from backend.database.models import Agent

from backend.trust_chain.schemas import (
    TrustChainRequest
)

from backend.trust_chain.service import (
    build_trust_chain
)

router = APIRouter()


@router.post("/trust-chain")
def create_chain(
    payload: TrustChainRequest,
    db: Session = Depends(get_db)
):

    research = db.query(Agent).filter(
        Agent.agent_id ==
        payload.research_agent_id
    ).first()

    review = db.query(Agent).filter(
        Agent.agent_id ==
        payload.review_agent_id
    ).first()

    security = db.query(Agent).filter(
        Agent.agent_id ==
        payload.security_agent_id
    ).first()

    if not all([
        research,
        review,
        security
    ]):
        raise HTTPException(
            status_code=404,
            detail="Agent not found"
        )

    return build_trust_chain(
        payload.finding,
        research,
        review,
        security
    )