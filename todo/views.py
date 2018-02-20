from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.utils import timezone


from .models import Action, ActionCategory
from .forms import ActionForm, ActionCategoryForm

@login_required
def action_list(request):
    first_category = None
    categories = None
    if (len(ActionCategory.objects.filter(author=request.user))>0):
        categories = ActionCategory.objects.filter(author=request.user)
        first_category = categories[0]
    actions = Action.objects.filter(category=first_category).order_by('-priority')
    return render(
        request, 
        'todo/sheet.html',
        {   'actions': actions,
            'categories': categories,
            'active_category': first_category   })

@login_required
def category_action_list(request, pk):
    category = get_object_or_404(ActionCategory, pk=pk)
    categories = ActionCategory.objects.filter(author=request.user)
    actions = Action.objects.filter(category=category).order_by('-priority')
    return render(
        request,
        'todo/sheet.html',
        {   'actions': actions,
            'categories': categories,
            'active_category': category
        })

@login_required
def update_action(request, pk):
    action = get_object_or_404(Action, pk=pk)
    categories = ActionCategory.objects.filter(author=request.user)
    if request.method == 'POST':
        form = ActionForm(request.POST, instance=action)
        if (form.is_valid):
            action = form.save()
            action.save()
            return redirect('category_action_list', pk=action.category.pk)
    else:
        form = ActionForm(instance=action)
        form.fields['category'].queryset = ActionCategory.objects.filter(author=request.user)
    return render(request, 'todo/action_edit.html', {'form': form, 'is_update': True, 'categories': categories})

@login_required
def create_action(request):
    categories = ActionCategory.objects.filter(author=request.user)
    if request.method == 'POST':
        form = ActionForm(request.POST)
        if (form.is_valid):
            action = form.save()
            action.save()
            return redirect('category_action_list', pk=action.category.pk)
    else:
        form = ActionForm()
        form.fields['category'].queryset = ActionCategory.objects.filter(author=request.user)
    return render(request, 'todo/action_edit.html', {'form': form, 'categories': categories})

@login_required
def create_action_category(request):
    categories = ActionCategory.objects.filter(author=request.user)
    if request.method == 'POST':
        form = ActionCategoryForm(request.POST)
        if (form.is_valid):
            action_category = form.save()
            action_category.author = request.user
            action_category.save()
            return redirect('category_action_list', pk=action_category.pk)
    else:
        form = ActionCategoryForm()
    return render(request, 'todo/category_edit.html', {'form': form, 'categories': categories})

@login_required
def update_action_category(request, pk):
    action_category = get_object_or_404(ActionCategory, pk=pk)
    categories = ActionCategory.objects.filter(author=request.user)
    if request.method == 'POST':
        form = ActionCategoryForm(request.POST, instance=action_category)
        if (form.is_valid):
            action_category = form.save()
            action_category.author = request.user
            action_category.save()
            return redirect('category_action_list', pk=action_category.pk)
    else:
        form = ActionCategoryForm(instance=action_category)
    return render(request, 'todo/category_edit.html', {'form': form, 'categories': categories, 'is_update': True})


@login_required
def delete_action(request, pk):
    action = get_object_or_404(Action, pk=pk)
    category_pk = action.category.pk
    action.delete()
    return redirect('category_action_list', pk=category_pk)

@login_required
def delete_action_category(request, pk):
    action_category = get_object_or_404(ActionCategory, pk=pk)
    action_category.delete()
    return redirect('action_list')

