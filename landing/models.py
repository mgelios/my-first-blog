from django.db import models
from django.utils import timezone


class SecretMessage(models.Model):
    sender = models.ForeignKey('auth.User', related_name='sender', on_delete=models.PROTECT)
    recepient = models.ForeignKey('auth.User', default=None, null=True, related_name='recepient', on_delete=models.PROTECT)
    text = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text