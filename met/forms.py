from django import forms
from  .models import met


class MetForm(forms.ModelForm):
    class Meta:
        model = met
        fields = '__all__'