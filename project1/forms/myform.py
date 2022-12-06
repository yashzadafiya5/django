from django import forms 

class Myform(forms.Form):
    number1=forms.IntegerField()
    number2=forms.IntegerField()

class MyBsForm(forms.Form):
    Name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label='Name',required=True)  
    
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}),label='Enter Your Email',required=True) 
    
    pasword=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),label='Enter your Password',required=True )
    
    country=[(1,'India'),(2,'us'),(3,'uk'),(4,'Austrailia'),(5,'china')]
    country=forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=country,required=True)

    languges=[(1,'gujrati'),(2,'hindi'),(3,'english')]
    languge=forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=languges)
    
    genders=[(1,'Male'),(0,'Female')]
    gender=forms.ChoiceField(widget=forms.RadioSelect,choices=genders)
    
    files=forms.FileField(widget=forms.FileInput(attrs={'class':'form-control','accept':'image/*'}),label='file input',required=True)