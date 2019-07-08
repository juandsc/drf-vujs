import requests


def client():
    # credentials = {'username': 'admin', 'password': 'admin2019'}
    # response = requests.post(
    #     'http://localhost:8000/api/rest-auth/login/', data=credentials
    # )
    token_header = 'Token 6866d542df715963641de672298c0759b20139d9'
    headers = {'Authorization': token_header}
    response = requests.get(
        'http://localhost:8000/api/profiles/', headers=headers
    )
    print(f'Status code: {response.status_code}')
    response_data = response.json()
    print(response_data)


if __name__ == "__main__":
    client()