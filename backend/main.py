from fastapi import FastAPI

app = FastAPI(
    title="AgentTrust",
    description="AI Agent Identity and Verification Platform",
    version="0.1.0"
)

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