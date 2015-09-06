# DailyDivider

I am a robot that tweets once every day at midnight (Pacific Time).

If you [follow me] than my tweets will act as daily dividers that separate regular tweets.

My creator and administrator is [@davidfstr]. Let him know if I am misbehaving.

[follow me]: https://twitter.com/DailyDivider
[@davidfstr]: https://twitter.com/davidfstr

## Prerequisites

* Python 2.7
    - I would use Python 3 but the `oauth2` library that this script uses does not support Python 3.

## Installation

```
pip install -r requirements.txt
```

## Configuration

* Copy `twitter_api_keys.py.template` to `twitter_api_keys.py` and insert
  appropriate API keys for a Twitter platform app that you have created on
  twitter.com.

## Usage

To post a tweet in the format `--- 2015-09-05, Saturday ---`, run the following command:

```
./daily_divider.py
```

Then you can configure cron or some other periodic task runner to invoke this script once per day.
