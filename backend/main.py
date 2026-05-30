from fastapi import FastAPI
from backend.agents.routes import router as agent_router

from backend.messages.routes import router as message_router



app = FastAPI(
    title="AgentTrust",
    description="AI Agent Identity and Verification Platform",
    version="0.1.0"
)

app.include_router(agent_router)
app.include_router(message_router)


@app.get("/")
def root():
    return {
        "message": "AgentTrust API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }