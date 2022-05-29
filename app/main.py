from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from routers import frontend, api

app = FastAPI()
app.include_router(frontend.router)
app.include_router(api.router)

app.mount("/assets", StaticFiles(directory="assets"), name="assets")
