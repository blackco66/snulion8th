from django.db import models
# 장고는 created_at과 updated_at을 알아서 만들어 주지 않음. id는 만들어 줌
from django.utils import timezone
from django.contrib.auth.models import User
from faker import Faker

# Create your models here.


class Feed(models.Model):  # 모델 클래스명은 단수형을 사용 (Feeds(x) Feed(O))
    # id는 자동 추가
    title = models.CharField(max_length=256)
    content = models.TextField()
    photo = models.ImageField(blank=True, upload_to='feed_photos')
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        User, blank=True, related_name='like_feeds', through='Like')

    def update_date(self):  # 나중에 수정할 때 사용
        self.updated_at = timezone.now()
        self.save()

    def update_feed(self, title, content):
        self.title = title
        self.content = content

    def __str__(self):
        return self.title


class FeedComment(models.Model):
    content = models.TextField()
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
