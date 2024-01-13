from fastapi.testclient import TestClient

from widget_server.app import app


def test_create_read_list():
    client = TestClient(app)
    # Create a new widget
    create_response = client.post(
        "/widgets/create",
        json={"name": "Foo"},
    )
    assert create_response.status_code == 200
    create_response_json = create_response.json()
    assert create_response_json == {
        "status": "success",
        "widget": {
            "id": create_response_json["widget"]["id"],
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
    assert create_response_json2 == {
        "status": "success",
        "widget": {
            "id": create_response_json2["widget"]["id"],
            "name": "Bar",
        },
    }

    # Read the widget back
    get_response = client.post(
        "/widgets/get",
        json={"id": create_response_json["widget"]["id"]},
    )
    assert get_response.status_code == 200
    get_response_json = get_response.json()
    assert get_response_json == {
        "status": "success",
        "widget": {
            "id": create_response_json["widget"]["id"],
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
                "id": create_response_json["widget"]["id"],
                "name": "Foo",
            },
            {
                "id": create_response_json2["widget"]["id"],
                "name": "Bar",
            },
        ],
    }
