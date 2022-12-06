from django import forms 

class Myform(forms.Form):
    hight=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='enter hight',required=True)
    width=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='enter width',required=True)
    text=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='text',required=True)