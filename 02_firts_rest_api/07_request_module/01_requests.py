import requests


def main():
    response = requests.get('https://api.exchangeratesapi.io/latest')
    
    if response.status_code != 200:
        print(f'Status code: {response.status_code}')
    
    print('Content-Type: {}'.format(response.headers['Content-Type']))
    data = response.json()
    print(f'JSON data: {data}')


if __name__ == "__main__":
    main()