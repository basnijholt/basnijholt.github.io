#!/usr/bin/env python

import feedparser
import yaml

feed = feedparser.parse('https://500px.com/basnijholt/rss')
ids = [int(entry['id'].split('/')[4]) for entry in feed['entries']]
with open('_data/photo_ids.yml', 'w') as f:
    yaml.dump(dict(ids=ids), f, default_flow_style=False)
