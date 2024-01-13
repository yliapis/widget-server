import uuid
from pydantic import BaseModel


# Core widget model


class Widget(BaseModel):
    id: str
    name: str


# Volatile internal widget store
# TODO: Replace with a persistent store

widget_store_table: dict[str, Widget] = {}


def create_widget(name: str) -> Widget:
    return Widget(
        id=str(uuid.uuid4()),
        name=name,
    )


def get_widget(id: str) -> Widget | None:
    return widget_store_table.get(id)
