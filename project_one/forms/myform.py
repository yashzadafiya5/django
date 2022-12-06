from django import forms 

class Myform(forms.Form):
    hight=forms.IntegerField()
    width=forms.IntegerField()