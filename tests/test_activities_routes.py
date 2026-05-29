def test_root_redirects_to_static_index(client):
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint, follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_all_seeded_activities(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)

    # Assert
    payload = response.json()
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert len(payload) == 9
    assert "Chess Club" in payload
    assert "Programming Class" in payload
