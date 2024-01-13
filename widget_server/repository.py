from datetime import datetime
import uuid
from pydantic import BaseModel

from sqlmodel import SQLModel, Session, select, Field, create_engine
from sqlmodel.pool import StaticPool


# Core widget model


class Widget(BaseModel):
    id: str
    name: str


# Widget sqlmodel


class _WidgetSQLModel(SQLModel, table=True):
    __tablename__ = "widgets"
    id: str = Field(primary_key=True)
    name: str
    date_created: datetime = Field(default_factory=datetime.utcnow)


# import all models from repository to ensure they are registered with SQLModel


# TODO: use real database during prod
#     engine = create_engine("sqlite:///database.db")
engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)

SQLModel.metadata.create_all(engine)


# helper functions to translate to/from sqlmodel


def _to_sqlmodel(widget: Widget) -> _WidgetSQLModel:
    return _WidgetSQLModel(
        id=widget.id,
        name=widget.name,
    )


def _from_sqlmodel(widget: _WidgetSQLModel) -> Widget:
    return Widget(
        id=widget.id,
        name=widget.name,
    )


# Widget repository


class WidgetRepository:
    def __init__(self):
        self._engine = engine  # TODO: inject

    def _insert_widget_record(self, widget: Widget) -> True:
        with Session(engine) as session:
            session.add(_to_sqlmodel(widget))
            session.commit()

    def _query_widget_record(self, id: str) -> Widget | None:
        with Session(engine) as session:
            if (sql_record := session.get(_WidgetSQLModel, id)) is not None:
                return _from_sqlmodel(sql_record)
            return None

    def _query_all_widget_records(self) -> list[Widget]:
        with Session(engine) as session:
            print(
                session.exec(
                    select(_WidgetSQLModel).order_by(_WidgetSQLModel.date_created)
                ).all()
            )
            return [
                _from_sqlmodel(record)
                for record in session.exec(select(_WidgetSQLModel)).all()
            ]

    def _update_widget_record(self, widget: Widget) -> Widget | None:
        with Session(engine) as session:
            if (sql_record := session.get(_WidgetSQLModel, widget.id)) is not None:
                sql_record.name = widget.name
                session.commit()
                return _from_sqlmodel(sql_record)
            return None

    def _delete_widget_record(self, id: str) -> bool:
        with Session(engine) as session:
            if (sql_record := session.get(_WidgetSQLModel, id)) is not None:
                session.delete(sql_record)
                session.commit()
                return True
            return False

    def _delete_all_widget_records(self) -> bool:
        with Session(engine) as session:
            for sql_record in session.exec(select(_WidgetSQLModel)).all():
                session.delete(sql_record)
            session.commit()
            return True

    def create_widget(self, name: str) -> Widget:
        new_widget = Widget(
            id=str(uuid.uuid4()),
            name=name,
        )
        self._insert_widget_record(new_widget)
        return new_widget

    def get_widget(self, id: str) -> Widget | None:
        return self._query_widget_record(id)

    def get_all_widgets(self) -> list[Widget]:
        return self._query_all_widget_records()

    def update_widget(self, id: str, name: str) -> Widget | None:
        return self._update_widget_record(Widget(id=id, name=name))

    def delete_widget(self, id: str) -> bool:
        return self._delete_widget_record(id)

    def delete_all_widgets(self) -> bool:
        return self._delete_all_widget_records()
