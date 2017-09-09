from django import forms
from django.core.exceptions import ValidationError

from .models import  Business_request, MyProfile , Pricing

BUSINESS_TYPE=( ('SERVICE','SERVICES' ),('MANUFACTURING','MANUFACTURING'),('SALES','SALES'),('PERSONAL','PERSONAL'),('SOCIETY','SOCIETY' ),('SCHOOL','SCHOOL'),('SUPER MARKER','SUPER MARKET'),)

def file_size(value): # Check File Size
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 2 MiB.')  


class BusinessRequestForm(forms.Form):
	business_name = forms.CharField(label='Enter Business Name', widget=forms.Textarea, help_text="Enter the Name of the business you require" )
	business_type= forms.ChoiceField(label='Select Your Business Type', choices=BUSINESS_TYPE, help_text="If your business type is not present. Enter details in Additional info" )
	license_type =forms.ModelChoiceField(label='Select the license type',queryset=Pricing.objects.none(),help_text="Check Pricing on Main Page Pricing")
	additional_detail=forms.CharField(label='Enter any additional details', widget=forms.Textarea, help_text="Give details about your Tax Structure", required=False)
	tax_structure=forms.CharField(label='Tax Structure ', widget=forms.Textarea, help_text="Describe Your Tax Structure If Applicable",required=False)
	sales_invoice=forms.FileField(help_text="Upload your present Sales Invoice if any",required=False)
	purchase_invoice=forms.FileField(help_text="Upload your present Purchase Invoice if any",required=False)
	pay_slip=forms.FileField(help_text="Upload your present Pay Slip if any",required=False)
	talley_file=forms.FileField(help_text="Upload your present Talley Export if any",required=False)
	
	def __init__(self,input_user,*args,**kwargs):
		super(BusinessRequestForm,self).__init__(*args,**kwargs)
		select_user=MyProfile.objects.get(user=input_user)
		price=Pricing.objects.all().filter(pricing_region=select_user.region).filter(target=select_user.sales_partner)
		self.fields['license_type'].queryset=price
		
		


 		
   
