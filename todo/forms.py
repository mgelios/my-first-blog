from django import forms
from .models import Action, ActionCategory

class ActionForm(forms.ModelForm):

    class Meta:
        model = Action
        fields = ('text', 'category',)


class ActionCategoryForm(forms.ModelForm):

    class Meta:
        model = ActionCategory
        fields = ('author', 'name',)