import requests


def main():
    response = requests.get("http://www.google.com")
    print(f'Status code: {response.status_code}')
    # print(f'Headers: {response.headers}')
    # print('Content-Type: {}'.format(response.headers['Content-Type']))
    print(f'Content: {response.text}')


if __name__ == "__main__":
    main()