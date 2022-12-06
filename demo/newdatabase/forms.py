from django import forms

class ragisterform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='password',required=True)