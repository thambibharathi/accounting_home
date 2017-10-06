from django import forms
from django.forms import ModelForm , Textarea
from django.core.exceptions import ValidationError
from mezzanine.accounts.forms import ProfileForm

from .models import  Business_request, MyProfile , Pricing

BUSINESS_TYPE=( ('SERVICE','SERVICES' ),('MANUFACTURING','MANUFACTURING'),('SALES','SALES'),('PERSONAL','PERSONAL'),('SOCIETY','SOCIETY' ),('SCHOOL','SCHOOL'),('SUPER MARKER','SUPER MARKET'),)

def file_size(value): # Check File Size
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')  


class BusinessRequestForm(ModelForm):
	class Meta:
		model=Business_request
		fields=['business_name','business_type','license_type','additional_details','tax_structure','sales_invoice','purchase_invoice','pay_slip','talley_file',]
		widgets = {'additional_details': Textarea(attrs={'cols': 80, 'rows': 20}),'tax_structure': Textarea(attrs={'cols': 80, 'rows': 20}) ,}
		
	def __init__(self,*args,**kwargs):
		self.request = kwargs.pop('request',None)
		super(BusinessRequestForm,self).__init__(*args,**kwargs)
		select_user=MyProfile.objects.get(user=self.request.user)
		price=Pricing.objects.all().filter(pricing_region=select_user.region).filter(target=select_user.sales_partner)
		self.fields['license_type'].queryset=price
		
		
class MyCustomProfileForm(ProfileForm):
    def save(self, *args, **kwargs):
        user = super(MyCustomProfileForm, self).save(*args, **kwargs)
        if self._signup:
            pass=self.cleaned_data.get('password1')
	    print(pass)
        return user
