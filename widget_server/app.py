from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4


app = FastAPI()


# Core widget model


class Widget(BaseModel):
    id: str
    name: str


# Volatile internal widget store
# TODO: Replace with a persistent store

widget_store_table: dict[str, Widget] = {}


# Create a widget


class CreateWidgetRequest(BaseModel):
    name: str


class CreateWidgetResponse(BaseModel):
    status: str
    widget: Widget | None


@app.post("/widgets/create", response_model=CreateWidgetResponse)
async def create_widget(request: CreateWidgetRequest):
    """
    Create a widget
    """
    new_widget = Widget(id=str(uuid4()), name=request.name)
    widget_store_table[new_widget.id] = new_widget
    return CreateWidgetResponse(
        status="success",
        widget=new_widget,
    )


# Read a widget by ID


class GetWidgetRequest(BaseModel):
    id: str


class GetWidgetResponse(BaseModel):
    status: str
    widget: Widget | None


@app.post("/widgets/get", response_model=GetWidgetResponse)
async def get_widget(request: GetWidgetRequest):
    """
    Get a widget by ID
    """
    if request.id not in widget_store_table:
        return GetWidgetResponse(
            status="error: widget not found",
            widget=None,
        )
    else:
        fetched_widget = widget_store_table[request.id]
        return GetWidgetResponse(
            status="success",
            widget=fetched_widget,
        )


# Read all widgets


class ListWidgetsResponse(BaseModel):
    status: str
    widgets: list[Widget]


@app.get("/widgets")
async def list_widgets():
    """
    Get all widgets
    """
    return ListWidgetsResponse(
        status="success",
        widgets=list(widget_store_table.values()),
    )


# Update a widget by ID


class UpdateWidgetRequest(BaseModel):
    id: str
    name: str


class UpdateWidgetResponse(BaseModel):
    status: str
    widget: Widget | None


@app.post("/widgets/update", response_model=UpdateWidgetResponse)
async def update_widget(request: UpdateWidgetRequest):
    """
    Update a widget by ID
    """
    if request.id not in widget_store_table:
        return UpdateWidgetResponse(
            status="error: widget not found to update",
            widget=None,
        )
    else:
        fetched_widget = widget_store_table[request.id]
        fetched_widget.name = request.name
        return UpdateWidgetResponse(
            status="success",
            widget=fetched_widget,
        )


# Delete a widget by ID


class DeleteWidgetRequest(BaseModel):
    id: str


class DeleteWidgetResponse(BaseModel):
    status: str


@app.post("/widgets/delete", response_model=DeleteWidgetResponse)
async def delete_widget(request: DeleteWidgetRequest):
    """
    Delete a widget by ID
    """
    if request.id not in widget_store_table:
        return DeleteWidgetResponse(
            status="error: widget not found to delete",
        )
    else:
        _ = widget_store_table.pop(request.id)
        return DeleteWidgetResponse(
            status="success",
        )


# Delete all widgets


class ClearWidgetsResponse(BaseModel):
    status: str


@app.delete("/widgets", response_model=ClearWidgetsResponse)
async def clear_widgets():
    """
    Delete all widgets
    """
    widget_store_table.clear()
    return ClearWidgetsResponse(
        status="success",
    )
