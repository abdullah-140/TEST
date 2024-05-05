from django import forms 
  
# creating a form  
class InputForm(forms.Form): 
    

  
    Processor = forms.CharField(max_length = 200) 
    RAM = forms.CharField(max_length = 200) 
    Storage = forms.CharField(max_length = 200) 
    graphics_card = forms.CharField(max_length = 200) 
    Motherboard = forms.CharField(max_length = 200) 
    Power_Supply  = forms.CharField(max_length = 200) 
    Case = forms.CharField(max_length = 200) 
