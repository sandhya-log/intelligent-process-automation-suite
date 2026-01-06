# from fastapi import FastAPI
# from backend.app.api.v1.routes import api_router

# app = FastAPI(
#     title="AE-V2-IPAS",
#     description="Intelligent Process Automation Suite",
#     version="1.0.0"
# )

# app.include_router(api_router, prefix="/api/v1")

# @app.get("/health")
# def health_check():
#     return {"status": "OK"}



from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.api.v1.routes import api_router

app = FastAPI(
    title="AE-V2-IPAS",
    description="Intelligent Process Automation Suite",
    version="1.0.0"
)

# ✅ CORS MIDDLEWARE (IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now (dev only)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

@app.get("/health")
def health_check():
    return {"status": "OK"}
