import requests


def client():
    # data = {
    #     'username': 'rest-test', 'email': 'rest-test@rest.com', 
    #     'password1': 'user2019', 'password2': 'user2019'
    # }
    # response = requests.post(
    #     'http://localhost:8000/api/rest-auth/registration/', data=data
    # )
    token_header = 'Token 8046d4d4e3812e5292e7ff11dfd7b364fe9fc349'
    headers = {'Authorization': token_header}
    response = requests.get(
        'http://localhost:8000/api/profiles/', headers=headers
    )
    print(f'Status code: {response.status_code}')
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()