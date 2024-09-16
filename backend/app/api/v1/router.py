from fastapi import FastAPI
import os
from fastapi import APIRouter

def setup_router(app: FastAPI):
    """
    Sets up the FastAPI application with the specified configuration.

    :param application: The FastAPI application to set up.
    """
    endpoints_path = os.path.join(os.path.dirname(__file__), "endpoints")
    for filename in os.listdir(endpoints_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            module = __import__(f"app.api.v1.endpoints.{module_name}", fromlist=["router"])
            if hasattr(module, "router") and isinstance(module.router, APIRouter):
                app.include_router(module.router, prefix=f"/api/v1/{module_name}")