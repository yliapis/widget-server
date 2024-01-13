import uuid
from pydantic import BaseModel


# Core widget model


class Widget(BaseModel):
    id: str
    name: str


# Volatile internal widget store
# TODO: Replace with a persistent store

_widget_store_table: dict[str, Widget] = {}


class WidgetRepository:
    def create_widget(self, name: str) -> Widget:
        new_widget = Widget(
            id=str(uuid.uuid4()),
            name=name,
        )
        _widget_store_table[new_widget.id] = new_widget
        return new_widget

    def get_widget(self, id: str) -> Widget | None:
        print("id: ", id)
        print("_widget_store_table: ", _widget_store_table)
        return _widget_store_table.get(id, None)

    def get_all_widgets(self) -> list[Widget]:
        return list(_widget_store_table.values())

    def update_widget(self, id: str, name: str) -> Widget | None:
        if id not in _widget_store_table:
            return None
        _widget_store_table[id].name = name
        return _widget_store_table[id]

    def delete_widget(self, id: str) -> bool:
        if id not in _widget_store_table:
            return False
        del _widget_store_table[id]
        return True

    def delete_all_widgets(self) -> bool:
        _widget_store_table.clear()
        return True
