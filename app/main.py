from fastapi import FastAPI
from app.api.v1.compliance import router as compliance_router

app = FastAPI(title="Grid Guard AI")

app.include_router(compliance_router)


@app.get("/")
def health():
    return {"status": "Grid Guard AI running"}