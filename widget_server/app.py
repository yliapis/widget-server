from fastapi import FastAPI
from pydantic import BaseModel


from widget_server.repository import (
    Widget,
    WidgetRepository,
)

app = FastAPI()

widget_repository: WidgetRepository = WidgetRepository()


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
    new_widget = widget_repository.create_widget(request.name)
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
    if (fetched_widget := widget_repository.get_widget(request.id)) is not None:
        return GetWidgetResponse(
            status="success",
            widget=fetched_widget,
        )
    else:
        return GetWidgetResponse(
            status="error: widget not found",
            widget=None,
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
        widgets=widget_repository.get_all_widgets(),
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
    if (
        updated_widget := widget_repository.update_widget(request.id, request.name)
    ) is not None:
        return UpdateWidgetResponse(
            status="success",
            widget=updated_widget,
        )
    else:
        return UpdateWidgetResponse(
            status="error: widget not found to update",
            widget=None,
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
    if not widget_repository.delete_widget(request.id):
        return DeleteWidgetResponse(
            status="error: widget not found to delete",
        )
    else:
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
    widget_repository.delete_all_widgets()
    return ClearWidgetsResponse(
        status="success",
    )
