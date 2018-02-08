from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Action, ActionCategory


@login_required
def task_list(request):
    category = None
    if (len(ActionCategory.objects.filter(author=request.user))>0):
        category = ActionCategory.objects.filter(author=request.user)[0]
    actions = Action.objects.filter(category=category)
    return render(request, 'todo/sheet.html', {'actions': actions})
