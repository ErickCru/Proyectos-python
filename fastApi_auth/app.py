from fastapi import FastAPI
from routes.user import user
from docs import tags_metadata

app = FastAPI(
    title="Rest Api With Fast Api and MongoDB",
    description="Example of REST API",
    version="1.0",
    openapi_tags=tags_metadata
)

app.include_router(user)
