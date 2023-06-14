import requests

def test_invalid_url():
    invalid_url = "https://reqres.in//api/users?page=invalid"
    response = requests.get(invalid_url)
    assert response.status_code == 404
    print("Page Not Found")


test_invalid_url()
