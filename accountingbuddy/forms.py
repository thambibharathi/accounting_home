from django import forms

from .models import  Business_request

class BusinessRequestForm(forms.ModelForm):
  class Meta:
    model=Business_request
    fields=['business_name','business_type','license_type','additional_details', ]  
    
  def __init__(self, *args, **kwargs):
        super(BusinessRequestForm, self).__init__(*args, **kwargs)
	user=MyProfile.objects.get(user=request.user) 
	price=Pricing.objects.all().filter(pricing_region=user.region).filter(target=user.sales_partner)
	self.license_type=forms.ModelChoiceField(queryset=price) 
