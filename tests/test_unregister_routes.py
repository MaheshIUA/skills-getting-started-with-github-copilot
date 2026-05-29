from src.app import activities


def test_unregister_removes_existing_participant(client):
    # Arrange
    activity_name = "Basketball"
    email = "liam@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {email} from {activity_name}"
    assert email not in activities[activity_name]["participants"]


def test_unregister_fails_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "student@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_fails_for_non_member(client):
    # Arrange
    activity_name = "Chess Club"
    email = "not.registered@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Participant not found in this activity"
