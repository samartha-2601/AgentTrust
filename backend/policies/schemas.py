from pydantic import BaseModel


class PolicyCheckRequest(BaseModel):
    agent_id: str
    action: str