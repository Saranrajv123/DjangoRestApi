import requests
import json

BASE_URL = "http://127.0.0.1:8000/"

ENDPOINT = 'api/update/'

def get_list():
    r = requests.get(BASE_URL + ENDPOINT)
    data = r.json()
    # print(json.dumps(data))
    for i in data:
        # print(i['id'])
        if i['id'] == 1:
            r2 = requests.get(BASE_URL + ENDPOINT + str(i['id']))
            print(r2.json())
            print(type(r2.json()))
    return data


# get_list()


def createupdate():
    new_data = {
        'user': 1,
        'content': 'new content'
    }

    req = requests.post(BASE_URL + ENDPOINT, data=new_data)
    print("status code", req.status_code)
    print('header', req.headers)
    if req.status_code == requests.codes.ok:
        # print(req.json())
        return req.json()
    return req.text


createupdate()
print('requests ', createupdate())
