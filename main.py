from fastapi import FastAPI
from routers.auth_router import router as auth_router
from routers.aircraft_router import router as aircraft_router

app = FastAPI()
app.include_router(auth_router)
app.include_router(aircraft_router, prefix="/aircraft")



