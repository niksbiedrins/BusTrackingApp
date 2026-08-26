from fastapi import FastAPI
from routers.stagecoach import router as stagecoach_router
from routers.bustimes import router as bustimes_router
app = FastAPI()
app.include_router(stagecoach_router)
app.include_router(bustimes_router)
