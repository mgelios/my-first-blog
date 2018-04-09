from django import forms
from .models import UtilitiesRecord, LivingPlace
from .models import IncomeRecord, ExpensesRecord, ExpensesCategory


class ExpensesCategoryForm(forms.ModelForm):

    class Meta:
        model = ExpensesCategory
        fields = ('name',)

class ExpensesRecordForm(forms.ModelForm):

    class Meta:
        model = ExpensesRecord
        fields = ('amount', 'date', 'name', 'comment', 'category',)

class IncomeRecordForm(forms.ModelForm):

    class Meta:
        model = IncomeRecord
        fields = ('amount', 'date', 'name', 'comment',)

class UtilityRecordForm(forms.ModelForm):

    class Meta:
        model = UtilitiesRecord
        fields = ('hot_water', 'cold_water', 'electricity', 'date', 'place',)


class LivingPlaceForm(forms.ModelForm):

    class Meta:
        model = LivingPlace
        fields = ('name', 'address',)