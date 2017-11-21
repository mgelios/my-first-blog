from django.db import models
from django.utils import timezone


class SecretMessage(models.Model):
    sender = models.ForeignKey('auth.User', related_name='sender')
    recepient = models.ForeignKey('auth.User', default=None, null=True, related_name='recepient')
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text