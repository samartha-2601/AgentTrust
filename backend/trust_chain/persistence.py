import uuid

from datetime import datetime

from backend.trust_chain.models import (
    TrustChain
)


def save_trust_chain(
    db,
    finding,
    research_agent,
    review_agent,
    security_agent,
    chain_valid
):

    chain = TrustChain(
        chain_id=str(uuid.uuid4()),
        finding=finding,
        research_agent=research_agent,
        review_agent=review_agent,
        security_agent=security_agent,
        chain_valid=chain_valid,
        timestamp=datetime.utcnow().isoformat()
    )

    db.add(chain)

    db.commit()

    db.refresh(chain)

    return chain