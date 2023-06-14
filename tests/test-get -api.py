import requests


def test_get_api_endpoint():
    url = "https://reqres.in/api/users?page=2"
    response = requests.get(url)
    response_data = response.json()
    user_data = response_data["data"][0]

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)
    print("Response JSON Data:", response_data)
    expected_data = {"first_name": "Michael", "last_name": "Lawson"}
    print("Expected Data:", expected_data)

    assert response.status_code == 200
    assert user_data["first_name"] == expected_data["first_name"]
    assert user_data["last_name"] == expected_data["last_name"]


test_get_api_endpoint()
