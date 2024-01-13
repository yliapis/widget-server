from sqlmodel import create_engine
from sqlmodel.pool import StaticPool

from widget_server.config import IS_TEST


print(IS_TEST)
if IS_TEST:
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    engine = create_engine("sqlite:///database.db")
