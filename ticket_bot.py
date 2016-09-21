#!/usr/local/virtualenvs/ds-py3/bin/python
import json
from time import sleep

import requests
import tweepy


SECRETS_FILE = "secrets.json"
TICKET_URL = "http://www.showclix.com/event/TheDailyShowWithTrevorNoah/recurring-event-times"
EVENT_STATUS_KEY = "event_status"
DATE_KEY = "time"
ON_SALE_STATUS = "on_sale
SOLD_OUT_STATUS = "sold_out"
POST_SALE_STATUS = "post_sale"
CHECK_INTERVAL = 5


def main():
    # Twitter API setup
    with open(SECRETS_FILE) as f:
        secrets = json.load(f)
    auth = tweepy.OAuthHandler(secrets['consumer_key'], secrets['consumer_secret'])
    auth.set_access_token(secrets['access_token'], secrets['access_secret'])
    api = tweepy.API(auth)

    ticket_dates = {}
    # Loop forever
    while 1 == 1:
        ticket_json = requests.get(TICKET_URL).json()
        for event in ticket_json['times']:
            event_status = event[EVENT_STATUS_KEY]
            event_date = event[DATE_KEY]
            if event_status == ON_SALE_STATUS and event_date not in ticket_dates:
                ticket_dates[event_date] = True
                msg = "{} tickets are available! ({})".format(event_date, event_status)
                send_msg(api, msg)
            elif (event_status in (SOLD_OUT_STATUS, POST_SALE_STATUS) and
                    event_date in ticket_dates):
                del ticket_dates[event_date]
                msg = "{} tickets are no longer available. ({})".format(event_date, event_status)
                send_msg(api, msg)
        sleep(CHECK_INTERVAL)


def send_msg(api, msg):
    try:
        status = api.send_direct_message(screen_name="florean", text=msg)
    except tweepy.error.TweepError as e:
        print(repr(e))


if __name__ == '__main__':
    main()
