from pydantic import BaseModel


class SignRequest(BaseModel):
    agent_id: str
    message: str


class VerifyRequest(BaseModel):
    agent_id: str
    message: str
    signature: str