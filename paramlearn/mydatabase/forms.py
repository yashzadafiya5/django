from django import forms 
from .models import ragister
class RagisterForm(forms.ModelForm):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password',required=True)
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='mobile',required=True)

    class Meta:
        model=ragister
        fields=('email','password','mobile')
class loginform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password',required=True)
    
class changepasswordform(forms.Form):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password',required=True)
    newpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='new Password',required=True)
    confirmnewpassword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='confirm new Password',required=True)

class forgotpasswordform(forms.Form):
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    
