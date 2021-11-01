import requests
import os
import json 

bearer_token = "AAAAAAAAAAAAAAAAAAAAAPhVVQEAAAAAjC6eYHqsvAsQlfCNacKyvDrfjI0%3DdBDTecTokHS4zsxGsrjLEBAoFYGnz5yM4G9oWuo71zGeaxp9KE"

url = "https://api.twitter.com/2/tweets/search/all"

query_params = {'query': '(from:twitterdev -is:retweet) OR #twitterdev','tweet.fields': 'author_id'}


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


if __name__ == "__main__":
    main()