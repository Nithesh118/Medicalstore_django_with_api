from django import forms
from .models import Medicine

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ['name', 'description', 'price','quantity']

from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

from django import forms
from .models import Customer
class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
            model = Customer
            fields = ['username', 'password', 'confirm_password']