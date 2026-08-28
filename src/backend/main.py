from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.stagecoach import router as stagecoach_router
from routers.bustimes import router as bustimes_router

app = FastAPI()

# middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(stagecoach_router)
app.include_router(bustimes_router)
