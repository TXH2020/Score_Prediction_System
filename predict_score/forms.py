from django import forms
from .models import Accept
class CForm(forms.ModelForm):
    data=forms.CharField(max_length=2,help_text="Enter number",required=False)
    class Meta:
        model=Accept
        fields = ('data',)