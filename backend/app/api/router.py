import os

from fastapi import FastAPI


def setup_router(app: FastAPI):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    for folder_name in os.listdir(current_dir):
        if folder_name.startswith("v") and os.path.isdir(
            os.path.join(current_dir, folder_name)
        ):
            router_file = os.path.join(current_dir, folder_name, "router.py")
            if os.path.isfile(router_file):
                module = __import__(
                    f"app.api.{folder_name}.router", fromlist=["setup_router"]
                )
                module.setup_router(app)
