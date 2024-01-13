# this needs to be imported to start the app
from widget_server.app import app  # noqa: F401

from fastapi.middleware.cors import CORSMiddleware
import uvicorn


# these are the origins that are allowed to access the API;
# these origins will come from the frontend run by node
origins = [
    "http://localhost:3000",
    "localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        # we pass in the app by string rather than by object since uvicorn requires it
        # for reloading
        "widget_server.server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info",
    )
