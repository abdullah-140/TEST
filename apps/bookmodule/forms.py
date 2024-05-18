from django import forms
from .models import PCS
from django.core.validators import EmailValidator
  
# creating a form  
class InputForm(forms.ModelForm): 
    class Meta:
        model = PCS
        fields = "__all__"
    
    Processor = forms.CharField(max_length = 200) 
    name = forms.CharField(max_length = 50)
    RAM = forms.CharField(max_length = 200) 
    Storage = forms.CharField(max_length = 200) 
    graphics_card = forms.CharField(max_length = 200) 
    Motherboard = forms.CharField(max_length = 200) 
    Power_Supply  = forms.CharField(max_length = 200) 
    Case = forms.CharField(max_length = 200) 
    price = forms.FloatField(min_value=0, max_value=10000)
    
class ContactForm(forms.Form):
    name = forms.CharField(max_length =100)
    email = forms.CharField(validators=[EmailValidator()])
    phone = forms.CharField(max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    
