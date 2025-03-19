import uvicorn
import uvloop
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from infra.databases.mongodatabase import MongoDatabase
from web.app.lecturers import lecturers_router
from web.app.students import students_router
from web.auth.auth import auth_router

api_version = '/api/v1'

app = FastAPI(
    title="Class Manager API",
    redirect_slashes=False,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix=api_version)
app.include_router(lecturers_router, prefix=api_version)
app.include_router(students_router, prefix=api_version)
app.add_event_handler("startup", MongoDatabase.connect)




if __name__ == "__main__":

    app_mode: str = os.getenv("APP_MODE", "development")

    uvicorn.run(
        "entrypoint:app",
        host="0.0.0.0",
        port=8000,
        lifespan="on",
        loop="uvloop",
        reload=True if app_mode == "development" else False
    )