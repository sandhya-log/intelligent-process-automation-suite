from fastapi import FastAPI
from backend.app.api.v1.routes import api_router

app = FastAPI(
    title="AE-V2-IPAS",
    description="Intelligent Process Automation Suite",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "OK"}
