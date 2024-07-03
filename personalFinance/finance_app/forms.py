from django import forms
from .models import YourFinance

class YourFinanceForm(forms.ModelForm):
    class Meta:
        model = YourFinance
        fields = ['date', 'amount', 'details']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    SPEND_OR_RECEIVE_CHOICES = [
        ('s', 'Spend'),
        ('r', 'Receive'),
    ]

    spend_or_receive = forms.ChoiceField(choices=SPEND_OR_RECEIVE_CHOICES)
