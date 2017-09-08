from django.shortcuts import render


from django.shortcuts import render, render_to_response
from django.shortcuts import get_object_or_404 , get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView , CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.utils import timezone
from django.template import loader
from django.http import HttpResponse
from django.http import Http404
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail

from accountingbuddy.models import MyProfile, Pricing, Business_request
from .forms import BusinessRequestForm 

# Create your views here.


def  pricing_india(request):
	if  request.user.is_authenticated:
		user=MyProfile.objects.get(user=request.user) 
		price=Pricing.objects.all().filter(pricing_region=user.region).filter(target=user.sales_partner)
		if price.count() > 0:		
			context={'price':price, }
		else :
			not_logged_in="True"
			context={'not_logged_in':not_logged_in,}
	else :
		not_logged_in="True"
		context={'not_logged_in':not_logged_in,  }	

	
	template_name="accountingbuddy/sales_price.html"
	return render(request,template_name,context)

@login_required
def businessRequestFormView(request):
	if request.method == 'POST':
		form = BusinessRequestForm(data=request.POST,input_user=request.user,)
		if form.is_valid():
			business_name=form.cleaned_data['business_name']
			business_type=form.cleaned_data['business_type']
			license_type=form.cleaned_data['license_type']
			additional_details=form.cleaned_data['additional_detail']
			s=Business_request(user=request.user,business_name=business_name,business_type=business_type,license_type=license_type,additional_details=additional_details)
			s.save()
			subject="AccountingBuddy.Org Business Setup Request Fm %s" % user.first_name
			message="Business Name : %s , Business Type: %s , License Type: %s, Additional Details : %s , User %s , Phone %s, Email %s" % (business_name,business_type,license_type, additional_details, request.user,user.myprofile.phone_no,user.email)
			recipients = ['keeganpatrao@gmail.com']
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect(reverse('accountingbuddy:thanks'))
	else:
		form = BusinessRequestForm(input_user=request.user)
	return render(request, 'business_request_form.html', {'form': form})
	
	





  
