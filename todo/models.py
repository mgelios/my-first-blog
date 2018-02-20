from django.db import models
from django.utils import timezone

ACTION_STATUSES = (
    (0, 'to do'),
    (1, 'in progress'),
    (2, 'done'),
)

ACTION_PRIORITIES = (
    (0, 'trivial'),
    (1, 'minor'),
    (2, 'normal'),
    (3, 'high'),
    (4, 'critical')
)

class Action(models.Model):
    text = models.CharField(default='', max_length=200)
    date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey('todo.ActionCategory', on_delete=models.CASCADE)
    status = models.IntegerField(default=0, choices=ACTION_STATUSES)
    priority = models.IntegerField(default=2, choices=ACTION_PRIORITIES)

    def __str__(self):
        return self.text


class ActionCategory(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None, null=True)
    name = models.CharField(default='', max_length=200)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
