from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from .models import Action, ActionCategory


@login_required
def task_list(request):
    first_category = None
    categories = None
    if (len(ActionCategory.objects.filter(author=request.user))>0):
        categories = ActionCategory.objects.filter(author=request.user)
        first_category = categories[0]
    actions = Action.objects.filter(category=first_category)
    return render(request, 'todo/sheet.html',
        {
            'actions': actions,
            'categories': categories,
            'active_category': first_category
        })
