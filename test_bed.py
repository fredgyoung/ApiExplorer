
# Docs: https://requests.readthedocs.io/en/latest/

import requests


def get_page(url, params=None):

    if params:
        response = requests.get(url, params=params)
    else:
        response = requests.get(url)

    '''
    print("REQUEST")
    print(f"URL: {response.request.url}")
    print(f"Method: {response.request.method}")
    print(f"Headers: {response.request.headers}")
    print("\nRESPONSE")
    print(f"Response: {response}")
    print(f"Headers: {response.headers}")
    '''

    if response.status_code != 200:
        print(f"Status Code {response.status_code}")

    try:
        json = response.json()
        print(f"JSON: {json}")
    except requests.exceptions.JSONDecodeError:
        pass

    # print(f"Text: {response.text}")


if __name__ == '__main__':

    payload = {'number': 10}
    get_page('http://dog-api.kinduff.com/api/facts', payload)
