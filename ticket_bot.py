#!/usr/local/virtualenvs/ds-py3/bin/python
import json

import requests
import tweepy


SECRETS_FILE = "secrets.json"
TICKET_URL = "http://www.showclix.com/event/TheDailyShowWithTrevorNoah/recurring-event-times"
EVENT_STATUS_KEY = "event_status"
DATE_KEY = "time"
ON_SALE_STATUS = "on_sale"


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
            event_status = event[EVENT_STATUS_KEY]
            event_date = event[DATE_KEY]
            if event_status == ON_SALE_STATUS:
                msg = "{} tickets are available! ({})".format(event_date, event_status)



if __name__ == '__main__':
    main()
