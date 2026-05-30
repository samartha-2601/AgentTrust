from pydantic import BaseModel


class AgentCreate(BaseModel):
    name: str
    role: str


class AgentResponse(BaseModel):
    agent_id: str
    name: str
    role: str
    public_key: str