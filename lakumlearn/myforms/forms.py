from django import forms 

class dateinput(forms.DateInput):
    input_type = 'date'
class Myform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='name',required=True)
    age=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='age',required=True)
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='email',required=True)
    mobile=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}),label='mobile',required=True)
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='password',required=True)
    photo=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','accept':'image/*'}),required=True)
    genders=[(1,'male'),(0,'Female')]
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=genders)
    countries=[(1,'india'),(2,'us'),(3,'uk'),(4,'australia')]
    country=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-select'}),label='country',choices=countries)
    
    hobbies=[(1,'singing'),(2,'song listning'),(3,'dancing'),(4,'travaling')]
    hobbi=forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=hobbies)
    
    textarea=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}),label='textarea input',required=True)
    
    birthdate=forms.DateField(widget=dateinput(attrs={'class':'form-control'}),label='date input',required=True)