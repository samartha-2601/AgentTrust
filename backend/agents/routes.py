import uuid

from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from backend.crypto.rsa_utils import generate_keypair

from backend.agents.schemas import AgentCreate

from backend.database.dependencies import get_db
from backend.database.models import Agent

router = APIRouter()


@router.post("/agents")
def create_agent(
    agent: AgentCreate,
    db: Session = Depends(get_db)
):

    private_key, public_key = generate_keypair()

    db_agent = Agent(
        agent_id=str(uuid.uuid4()),
        name=agent.name,
        role=agent.role,
        public_key=public_key,
        private_key=private_key
    )

    db.add(db_agent)

    db.commit()

    db.refresh(db_agent)

    return {
        "agent_id": db_agent.agent_id,
        "name": db_agent.name,
        "role": db_agent.role,
        "public_key": db_agent.public_key
    }


@router.get("/agents")
def list_agents(
    db: Session = Depends(get_db)
):

    agents = db.query(Agent).all()

    return [
        {
            "agent_id": a.agent_id,
            "name": a.name,
            "role": a.role,
            "public_key": a.public_key
        }
        for a in agents
    ]