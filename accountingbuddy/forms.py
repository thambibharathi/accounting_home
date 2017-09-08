from django import forms

from .models import  Business_request

class BusinessRequestForm(forms.ModelForm):
  class Meta:
    model=Business_request
    fields=['business_name','business_type','license_type','additional_details', ]  

