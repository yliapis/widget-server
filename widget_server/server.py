
# this needs to be imported to start the app
from widget_server.app import app  # noqa: F401

import uvicorn

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
