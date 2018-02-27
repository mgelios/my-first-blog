from django.db import models
from django.utils import timezone

import json
import urllib
from datetime import timedelta
from datetime import datetime, timezone

from django.shortcuts import get_object_or_404

from dashboard.models import RadiotArticle

LATENCY_DAYS=1
SECONDS_IN_DAY=86400

BASE_API_URL = 'https://news.radio-t.com/api/v1/'
LAST_NEWS_API_SUFFIX = 'news/last/100'

def update_info():
    test_article = None
    try:
        if (len(RadiotArticle.objects.filter()) > 0):
            test_article = RadiotArticle.objects.filter()[0]
    except RadiotArticle.DoesNotExist:
        test_article = None

    if (test_article == None):
        get_info()
    else:
        last_updated = test_article.last_updated
        from_last_update = (datetime.now(timezone.utc) - last_updated).total_seconds()
        from_last_update = int(from_last_update / SECONDS_IN_DAY)
        if (from_last_update >= LATENCY_DAYS):
            get_info()

def get_info():
    news = get_raw_info()
    RadiotArticle.objects.filter().delete()
    for article in news:
        db_article = RadiotArticle.objects.create()
        db_article.title = article['title']
        db_article.content = article['content']
        db_article.snippet = article['snippet']
        db_article.main_pic = article['pic']
        db_article.link = article['link']
        db_article.author = article['author']
        db_article.original_ts = article['ts']
        db_article.radiot_ts = article['ats']
        db_article.feed = article['feed']
        db_article.slug = article['slug']
        db_article.comments = article['comments']
        db_article.likes = article['likes']
        db_article.save()

def get_raw_info():
    json_content = []
    try:
        content = urllib.request.urlopen(BASE_API_URL + LAST_NEWS_API_SUFFIX).read().decode('utf-8')
        json_content = json.loads(content)
    except urllib.error.HTTPError as e:
        print("error during fetching radiot news")
        print(e)
    return json_content

