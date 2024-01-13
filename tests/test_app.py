from fastapi.testclient import TestClient

from widget_server.app import app


def test_app_basic_client_usage():
    """
    Sequential client usage of the API

    # TODO: split this up and organize it more; it is currently a bit unruley
    """
    client = TestClient(app)
    # Create a new widget
    create_response = client.post(
        "/widgets/create",
        json={"name": "Foo"},
    )
    assert create_response.status_code == 200
    create_response_json = create_response.json()
    foo_widget_id = create_response_json["widget"]["id"]
    assert create_response_json == {
        "status": "success",
        "widget": {
            "id": foo_widget_id,
            "name": "Foo",
        },
    }

    # Create another widget
    create_response2 = client.post(
        "/widgets/create",
        json={"name": "Bar"},
    )
    assert create_response2.status_code == 200
    create_response_json2 = create_response2.json()
    bar_widget_id = create_response_json2["widget"]["id"]
    assert create_response_json2 == {
        "status": "success",
        "widget": {
            "id": bar_widget_id,
            "name": "Bar",
        },
    }

    # Read the widget back
    get_response = client.post(
        "/widgets/get",
        json={"id": foo_widget_id},
    )
    assert get_response.status_code == 200
    get_response_json = get_response.json()
    assert get_response_json == {
        "status": "success",
        "widget": {
            "id": foo_widget_id,
            "name": "Foo",
        },
    }

    # List all widgets
    list_response = client.get("/widgets")
    assert list_response.status_code == 200
    list_response_json = list_response.json()
    assert list_response_json == {
        "status": "success",
        "widgets": [
            {
                "id": foo_widget_id,
                "name": "Foo",
            },
            {
                "id": bar_widget_id,
                "name": "Bar",
            },
        ],
    }

    # update the Bar widget to Baz
    update_response = client.post(
        "/widgets/update",
        json={
            "id": bar_widget_id,
            "name": "Baz",
        },
    )

    assert update_response.status_code == 200
    update_response_json = update_response.json()
    assert update_response_json == {
        "status": "success",
        "widget": {
            "id": bar_widget_id,
            "name": "Baz",
        },
    }
    baz_widget_id = bar_widget_id
    bar_widget_id = None

    # Read the widget back
    get_response = client.post(
        "/widgets/get",
        json={"id": baz_widget_id},
    )
    assert get_response.status_code == 200
    get_response_json = get_response.json()
    assert get_response_json == {
        "status": "success",
        "widget": {
            "id": baz_widget_id,
            "name": "Baz",
        },
    }

    # Delete the Foo widget
    delete_response = client.post(
        "/widgets/delete",
        json={"id": foo_widget_id},
    )
    assert delete_response.status_code == 200
    delete_response_json = delete_response.json()
    assert delete_response_json == {"status": "success"}

    # Read the widget back
    get_response = client.post(
        "/widgets/get",
        json={"id": foo_widget_id},
    )
    assert get_response.status_code == 200
    get_response_json = get_response.json()
    assert get_response_json == {
        "status": "error: widget not found",
        "widget": None,
    }

    # List all widgets
    list_response = client.get("/widgets")
    assert list_response.status_code == 200
    list_response_json = list_response.json()
    assert list_response_json == {
        "status": "success",
        "widgets": [
            {
                "id": baz_widget_id,
                "name": "Baz",
            },
        ],
    }
