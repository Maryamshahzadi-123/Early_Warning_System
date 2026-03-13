from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.radar_router import router as radar_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(radar_router, prefix="/radar")
