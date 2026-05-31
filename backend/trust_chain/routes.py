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

from backend.trust_chain.persistence import (
    save_trust_chain
)

from backend.trust_chain.models import (
    TrustChain
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

    result = build_trust_chain(
        payload.finding,
        research,
        review,
        security
    )

    save_trust_chain(
        db=db,
        finding=payload.finding,
        research_agent=research.name,
        review_agent=review.name,
        security_agent=security.name,
        chain_valid=result["chain_valid"]
    )

    return result


@router.get("/trust-chain")
def list_trust_chains(
    db: Session = Depends(get_db)
):

    chains = db.query(
        TrustChain
    ).all()

    return [
        {
            "chain_id": c.chain_id,
            "finding": c.finding,
            "research_agent": c.research_agent,
            "review_agent": c.review_agent,
            "security_agent": c.security_agent,
            "chain_valid": c.chain_valid,
            "timestamp": c.timestamp
        }
        for c in chains
    ]