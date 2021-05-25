import pytest
import requests
import json
import time
import fixtures


@pytest.mark.webtest
def test_dummy_id():
    """test unexisting task"""
    data = json.loads(requests.get("http://127.0.0.1:5000/tags/1.5").text)

    expected_output = json.loads('{"ready": false, "state": "PENDING"}')
    assert data == expected_output


@pytest.mark.webtest
def test_google():
    """test standard flow"""
    response = requests.post(
        "http://127.0.0.1:5000/tags",
        json=fixtures.json_google
    )
    task_id = response.json()["task_id"]

    time.sleep(1)
    data = requests.get("http://127.0.0.1:5000/tags/"+task_id).text

    expected_output = json.loads(fixtures.google_tags)
    assert json.loads(data) == expected_output


@pytest.mark.slow
def test_long_task():
    """test long task change status to finished"""
    response = requests.post(
        "http://127.0.0.1:5000/tags_long",
        json=fixtures.json_google
    )
    task_id = response.json()["task_id"]

    data1 = requests.get("http://127.0.0.1:5000/tags/"+task_id).text
    time.sleep(20)
    data2 = requests.get("http://127.0.0.1:5000/tags/"+task_id).text

    assert data1 != data2
    assert "the_data" in data2
