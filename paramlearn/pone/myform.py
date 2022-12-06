from django import forms 

class Myform(forms.Form):
    hight=forms.IntegerField()
    width=forms.IntegerField()
    
class MyBsform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='name',required=True)
    age=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='age',required=True)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required= True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Password',required=True)
    languges=[(1,'english'),(2,'hindi'),(3,'gujrati')]
    languge=forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=languges,required=True)
    gender=[(1,'male'),(0,'Female')]
    genders=forms.ChoiceField(widget=forms.RadioSelect,required=True,choices=gender)
    country=[(1,'india'),(2,'uk'),(3,'us'),(4,'australia'),]
    countrys=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select'}),required=True,choices=country ,label='country')
    description=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}),label='enter description')
    
    files=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','accept':'image/*'}),label='select file',required=True)