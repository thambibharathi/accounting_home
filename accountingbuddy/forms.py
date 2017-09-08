from django import forms

from .models import  Business_request, MyProfile , Pricing

BUSINESS_TYPE=( ('SERVICE','SERVICES' ),('MANUFACTURING','MANUFACTURING'),('SALES','SALES'),('PERSONAL','PERSONAL'),('SOCIETY','SOCIETY' ),('SCHOOL','SCHOOL'),('SUPER MARKER','SUPER MARKET'),)

class BusinessRequestForm(forms.Form):
	business_name = forms.CharField(label='Enter Business Name', widget=forms.Textarea, help_text="Enter the Name of the business you require" )
	business_type= forms.ChoiceField(label='Select Your Business Type', choice=BUSINESS_TYPE, help_text="If your business type is not present. Enter details in Additional info" )
	license_type =forms.ModelChoiceField(label='Select the license type',queryset=Pricing.objects.none(),help_text="Check Pricing on Main Page Pricing")
	additional_detail=forms.CharField(label='Enter any additional details', widget=forms.Textarea, help_text="Give details about your Tax Structure", required=False)
	
	def __init__(self,user,*args,**kwargs):
		super(BusinessRequestForm,self).__init__(*args,**kwargs)
		select_user=MyProfile.objects.get(user=user)
		price=Pricing.objects.all().filter(pricing_region=select_user.region).filter(target=select_user.sales_partner)
		self.fields['license_type'].queryset=price
		
		
   		
   
