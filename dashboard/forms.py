from django import forms
from .models import UtilitiesRecord, LivingPlace

class UtilityRecordForm(forms.ModelForm):

    class Meta:
        model = UtilitiesRecord
        fields = ('hot_water', 'cold_water', 'electricity', 'date', 'place',)


class LivingPlaceForm(forms.ModelForm):

    class Meta:
        model = LivingPlace
        fields = ('name', 'address',)