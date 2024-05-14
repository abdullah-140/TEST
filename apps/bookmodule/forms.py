from django import forms
from .models import PCS
  
# creating a form  
class InputForm(forms.ModelForm): 
    class Meta:
        model = PCS
        fields = "__all__"
    

  
    Processor = forms.CharField(max_length = 200) 
    RAM = forms.CharField(max_length = 200) 
    Storage = forms.CharField(max_length = 200) 
    graphics_card = forms.CharField(max_length = 200) 
    Motherboard = forms.CharField(max_length = 200) 
    Power_Supply  = forms.CharField(max_length = 200) 
    Case = forms.CharField(max_length = 200) 
