from django import forms 
from .models import categorys 

class RagisterForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='title',required=True)
    photo=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}),label='image',required=True)
    class Meta:
        model=categorys
        fields=('title','photo')