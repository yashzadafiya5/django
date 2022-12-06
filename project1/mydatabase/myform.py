from django import forms 
from .models import user


class RagisterForm(forms.ModelForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password',required=True)
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='mobile',required=True)
    class Meta:
        model=user
        fields=('email','password','mobile')
class loginform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password',required=True)
    
class changepasswordform(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='current password',required=True)
    newpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='new password',required=True)
    confiremnewpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='confirem new   password',required=True)

class forgetpasswordform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)