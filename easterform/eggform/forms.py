from django import forms
from eggform.models import Eggs

eggCount = [('50',50),('100',100)]

class EggForm(forms.ModelForm):
    eggs = forms.ChoiceField(choices=eggCount, widget=forms.RadioSelect(),label='Number of Eggs?')
    payEmail = forms.EmailField(label = 'PayPal Email')
    number = forms.CharField(label = 'Phone Number')
    class Meta:
        model = Eggs
        fields = '__all__'
