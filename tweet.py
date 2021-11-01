import requests
import os
import json

bearer_token = os.environ.get('TWITTER_BEARER_TOKEN')

def create_url():
    tweet_fields = "tweet.fields=lang,author_id"
    ids = "1278747501642657792,1255542774432063488"
    url = f"https://api.twitter.com/2/tweets?{ids}&{tweet_fields}"

    return url

def bearer_oauth(r):
    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] ="v2TweetLookupPython"

    return r


def connect_to_endpoint(url):
    response = requests.request("GET", url, auth=bearer_oauth)
    print(response.status_code)

    if response.status_code != 200:
        raise Exception(
            f"Request returned an error: {response.status_code} {response.text}"
        )
    return response.json()

def main():
    url = create_url()
    json_response = connect_to_endpoint(url)
    print(json.dumps(json_response, indent=4, sort_keys=True))

if __name__ == "__main__":
    main()
