import requests
import json
import re


def test_image_urls_and_email_format():

    response = requests.get("https://reqres.in/api/users?page=2")
    data = response.json()

    print("Response Status Code:", response.status_code)
    print("Response Content:", response.content)
    print("Response JSON Data:", response.json())


    image_urls = ["michael.lawson@reqres.in"]
    email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    for item in data['data']:
        avatar_url = item.get('avatar')
        email = item.get('email')

        assert avatar_url is not None
        assert re.match(r'^https?://.*\.(jpeg|jpg|png|gif)$', avatar_url, re.IGNORECASE) is not None

        assert email is not None
        assert re.match(email_pattern, email) is not None
        assert response.status_code == 200

    print("All image URLs and email formats are valid.")


test_image_urls_and_email_format()
