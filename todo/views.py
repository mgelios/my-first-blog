from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Action, ActionCategory


@login_required
def task_list(request):
    category = ActionCategory.objects.filter()
    actions = Actions.objects.filter('')
    return None
