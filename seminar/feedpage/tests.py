from django.test import TestCase
from django.test import Client
from .models import Feed
import json


class FeedTest(TestCase):

    def test_update(self):
        feed = Feed.objects.create(title="test_title", content="test_content")

        feed.update_feed("changed_title", "changed_content")

        assert feed.title == "changed_title"
        assert feed.content == "changed_content"
