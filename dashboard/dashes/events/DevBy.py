from django.db import models
from django.utils import timezone

import json
import urllib
import feedparser

from datetime import timedelta
from datetime import datetime, timezone
from django.shortcuts import get_object_or_404

from dashboard.models import DevByEvent


RSS_URL = 'https://events.dev.by/rss'
LATENCY_DAYS=1
SECONDS_IN_DAY=86400



def update_info():
    test_event = None
    try:
        if (len(DevByEvent.objects.filter())>0):
            test_event = DevByEvent.objects.filter()[0]
    except DevByEvent.DoesNotExist:
        test_event = None

    if test_event != None :
        last_updated = test_event.last_updated
        from_last_update = (datetime.now(timezone.utc) - last_updated).total_seconds()
        from_last_update = int(from_last_update / SECONDS_IN_DAY)
        if (from_last_update >= LATENCY_DAYS):
            get_info()
    else:
        get_info()

def get_info():
    feed = get_raw_info()
    DevByEvent.objects.filter().delete()
    if (feed != None):
        for entry in feed:
            event_db = DevByEvent.objects.create()
            event_db.title = str(entry['title'])
            event_db.content = str(entry['description']).replace('<em>','').replace('<strong>', '').replace('</strong>', '')
            event_db.link = str(entry['link'])
            event_db.save()

def get_raw_info():
    feed = None
    try:
        feed = feedparser.parse(RSS_URL)
        return feed['entries']
    except Exception as e:
        print('error during fetching dev by feed')
    return feed
