# app/app.py

from contextlib import asynccontextmanager
from fastapi import FastAPI
#from .openapi import custom_openapi
import os
from app.api.router import setup_router

from app.core.logger import setup_logger

logger = setup_logger()

def on_startup():
    """
    Sets up the FastAPI application on startup.
    """
    logger.info("Setting up FastAPI application")
    setup_router(app)

def on_shutdown():
    """
    Tears down the FastAPI application on shutdown.
    """
    logger.info("Tearing down FastAPI application")
    pass

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Sets up the FastAPI application with the specified configuration.

    :param application: The FastAPI application to set up.
    """
    on_startup()
    yield
    on_shutdown()

app_informations = {
    "title": "Blog API",
    "version": "1.0.0",
    "description": "API for managing articles and tags in a blog",
}

if os.getenv("RUN_MODE") == "DEV":
    logger.info("Running in DEV mode")
    app = FastAPI(lifespan=lifespan, **app_informations)
else:
    logger.info("Running in PROD mode")
    app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, **app_informations)

