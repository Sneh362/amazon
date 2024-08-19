from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'category']


class LoginForm(forms.Form):
    username = forms.CharField(max_length=1)
    password = forms.CharField(widget=forms.PasswordInput)
    age = forms.IntegerField()

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age and (age < 0 or age > 12):
            raise forms.ValidationError('Age must be between 0 and 120.')
        return age
