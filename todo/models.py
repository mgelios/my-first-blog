from django.db import models
from django.utils import timezone


class Action(models.Model):
    text = models.CharField(default='', max_length=200)
    date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('todo.ActionCategory', on_delete=models.PROTECT)


class ActionCategory(models.Model):
    name = models.CharField(default='', max_length=200)
    last_updated = models.DateTimeField(timezone.now)