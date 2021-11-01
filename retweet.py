import requests
import os
import json

bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

def create_url():
    user_fields = "user.fields=created_at,description"
    id = "1454878780334477316"
    url  = "https://api.twitter.com/2/tweets/{}/retweeted_by".format(id)

    return url, user_fields


def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RetweetedByPython"
    return r

def connect_to_endpoint(url, user_fields):
    response = requests.request("GET", url, auth=bearer_oauth, params=user_fields)
    print(response.status_code)

    if response.status_code != 200:
        raise Exception(
            f"Request returned and error: {response.status_code} {response.text}"
        )
    return response.json()


def main():
    url, user_fields = create_url()
    json_response = connect_to_endpoint(url, user_fields)
    print(json.dumps(json_response, indent=4, sort_keys=True))
if __name__ == "__main__":
    main()