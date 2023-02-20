from django import forms 
from .models import ragister,incident

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
    
class Myincident(forms.ModelForm):
    locations = [(1,'India'),(2,'US'),(3,'UK'),(4,'Canada'),(5,'Australia')]
    location = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=locations,label="Select location")
    incidentdepartment = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols': '10', 'rows': '3'}),label="Incident Department",required=True)
    
    incidentlocation = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Incident Location",required=True)
    
    incidentsevierys = [(1,'Mild'),(2,'US'),(3,'UK'),(4,'Canada'),(5,'Australia')]
    incidentseviery = forms.ChoiceField(widget=forms.Select(attrs={'class':'form-control'}),choices=incidentsevierys,label="Select country") 
    
    suspectcause = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols': '10', 'rows': '3'}),label="Suspect Cause",required=True)
    
    immediateactiontaken = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','cols': '10', 'rows': '3'}),label="Immediate Action Taken",required=True)
    
    subincidenttypes=[(1,'Environmental incident'),(2,'injury/illness'),(3,'Property damage'),(4,'Vehical')]
    subincidenttype=forms.ChoiceField(widget=forms.CheckboxSelectMultiple,choices=subincidenttypes,label='Sub Incident Types')
    
    reportedby = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),label="Reported By",required=True)
    
    class Meta:
        model=incident
        fields=('location','incidentdepartment','incidentlocation','incidentseviery','suspectcause','immediateactiontaken','subincidenttype','reportedby')