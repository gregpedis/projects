import os
import json
import requests as req
import configparser as cp
from datetime import datetime as dt
from requests_oauthlib import OAuth1Session as session

config = cp.ConfigParser()
config.read('config.ini')


def get_twitter_session():
    api, token = config['api'], config['token']
    a_key, a_secret = api['key'], api['secret']
    t_key, t_secret = token['key'], token['secret']

    twitter = session(
        client_key=a_key,
        client_secret=a_secret,
        resource_owner_key=t_key,
        resource_owner_secret=t_secret)
    return twitter


def get_inspirobot_bytes():
    base_url = config['default']['inspirobot_url']
    generated_url = req.get(base_url).text
    result = req.get(generated_url)
    return result.content


def get_media_id(ss):
    url = config['default']['media_url']
    img_bytes = get_inspirobot_bytes()
    res = ss.post(url, files={'media': img_bytes})
    values = json.loads(res.text)
    return values['media_id']


def get_pretty_date_now():
    return dt.now().strftime("%Y-%m-%d, %A of %B.")


def tweet():
    twitter = get_twitter_session()

    base_url = config['default']['tweet_url']
    pretty_date = get_pretty_date_now()
    media_id = get_media_id(twitter)

    url = f'{base_url}?status=Posted at {pretty_date}&media_ids={media_id}'
    return twitter.post(url)


if __name__ == "__main__":
    res = tweet()
    pass
