import uuid

from fastapi import APIRouter
from backend.crypto.rsa_utils import generate_keypair
from backend.agents.schemas import AgentCreate

router = APIRouter()


AGENTS = []


@router.post("/agents")
def create_agent(agent: AgentCreate):

    private_key, public_key = generate_keypair()

    agent_record = {
        "agent_id": str(uuid.uuid4()),
        "name": agent.name,
        "role": agent.role,
        "public_key": public_key,
        "private_key": private_key
    }

    AGENTS.append(agent_record)

    return {
        "agent_id": agent_record["agent_id"],
        "name": agent_record["name"],
        "role": agent_record["role"],
        "public_key": public_key
    }


@router.get("/agents")
def list_agents():
    return AGENTS