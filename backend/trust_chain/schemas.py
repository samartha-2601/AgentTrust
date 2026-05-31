from pydantic import BaseModel


class TrustChainRequest(BaseModel):
    finding: str
    research_agent_id: str
    review_agent_id: str
    security_agent_id: str