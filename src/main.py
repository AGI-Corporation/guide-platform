"""
G.U.I.D.E. Platform - Main Application Entry Point

Growth · Understanding · Intent · Donations · Escalation
Human-Centered AI for Customer Service & Philanthropy
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.v1.router import api_router
from src.core.config import settings
from src.core.logging import setup_logging

setup_logging()

app = FastAPI(
    title="G.U.I.D.E. Platform API",
    description="Human-Centered AI for Customer Service & Philanthropy",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/v1")


@app.get("/health")
async def health_check() -> dict:
    """Health check endpoint."""
    return {"status": "healthy", "version": "0.1.0"}
