#!/usr/local/virtualenvs/ds-py3/bin/python
import json

import requests
import tweepy

SECRETS_FILE = "secrets.json"


def main():
    # Twitter API setup
    with open(SECRETS_FILE) as f:
        secrets = json.load(f)
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])
    api = tweepy.API(auth)

    # Loop forever
    while True:
        ticket_json = requests.get(TICKET_URL).json()
        for event in ticket_json['times']:
            pass


if __name__ == '__main__':
    main()
