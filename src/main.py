from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from src.routers.stagecoach import router as stagecoach_router
from src.routers.bustimes import router as bustimes_router

app = FastAPI()

app.include_router(stagecoach_router)
app.include_router(bustimes_router)

app.mount(
    "/",
    StaticFiles(directory=Path(__file__).parent / "static", html=True),
    name="static",
)
