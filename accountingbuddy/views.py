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
from django.core.mail import send_mail , BadHeaderError
from django.core.files.storage import FileSystemStorage
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import EmailMultiAlternatives

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
'''
@login_required
def businessRequestFormView(request):
	if request.method == 'POST':
		form = BusinessRequestForm(request.FILES,data=request.POST,input_user=request.user,)
		if form.is_valid():
			business_name=form.cleaned_data['business_name']
			business_type=form.cleaned_data['business_type']
			license_type=form.cleaned_data['license_type']
			additional_details=form.cleaned_data['additional_detail']
			tax_structure=form.cleaned_data['tax_structure']
			s=Business_request()
			s.user=request.user
			s.business_name=business_name
			s.business_type=business_type
			s.license_type=license_type
			s.additional_details=additional_details
			if request.FILES['sales_invoice']:
				sales_invoice=request.FILES['sales_invoice']
				s.sales_invoice=sales_invoice
			if request.FILES['purchase_invoice']:
				purchase_invoice=request.FILES['purchase_invoice']
				s.purchase_invoice=purchase_invoice
			if request.FILES['pay_slip']:
				pay_slip=request.FILES['pay_slip']
				s.pay_slip=pay_slip
			if request.FILES['talley_file']:
				talley_file=request.FILES['talley_file']
				s.talley_file=talley_file
			s.save()
			user=request.user
			sender='info@accountingbuddy.org'
			subject="AccountingBuddy.Org Business Setup Request Fm %s" % user.first_name
			message="Business Name : %s , Business Type: %s , License Type: %s, Additional Details : %s , User %s , Phone %s, Email %s" % (business_name,business_type,license_type, additional_details, request.user,user.myprofile.phone_no,user.email)
			recipients = ['keeganpatrao@gmail.com',]
			recipients +=[user.email,]
			send_mail(subject, message, sender, recipients)
			return HttpResponseRedirect(reverse('accountingbuddy:thanks'))
	else:
		form = BusinessRequestForm(input_user=request.user)
	return render(request, 'business_request_form.html', {'form': form})
	
'''

@login_required
def businessRequestFormView(request):
	if request.method == 'POST':
		form=BusinessRequestForm(request.POST,request.FILES,request=request)
		if form.is_valid():
			#s=Business_request(user=request.user)
			busreq=form.save(commit=False)
			busreq.user=request.user
			busreq.save()
			user=request.user
			from_email='info@accountingbuddy.org'
			subject="AccountingBuddy.Org Business Setup Request Fm %s" % user.first_name
			text_content="Business Name : %s , Business Type: %s , License Type: %s, Additional Details : %s , User %s , Phone %s, Email %s" % (busreq.business_name,busreq.business_type,busreq.license_type, busreq.additional_details, request.user,user.myprofile.phone_no,user.email)
			html_content=" <h4> Business Set Up Request </h4> <br> <ul> <li> Business Name : %s  </li> <li> Business Type : %s  </li> <li> License Type : %s  </li> <li> Additional Details : %s  </li><li> User : %s  </li><li> Phone : %s  </li><li> Email : %s  </li> </ul>" % (busreq.business_name,busreq.business_type,busreq.license_type, busreq.additional_details, request.user,user.myprofile.phone_no,user.email)
			to = ['keeganpatrao@gmail.com',]
			to +=[user.email,]
			msg = EmailMultiAlternatives(subject, text_content, from_email, to)
			msg.attach_alternative(html_content, "text/html")
			if busreq.sales_invoice.name is not '':
				message.attach_file(busreq.sales_invoice.path)
			if busreq.purchase_invoice.name is not '':
				message.attach_file(busreq.purchase_invoice.path)
			if busreq.pay_slip.name is not '':
				message.attach_file(busreq.pay_slip.path)
			if busreq.talley_file.name is not '':
				message.attach_file(busreq.talley_file.path)	
			msg.send()
			return HttpResponseRedirect(reverse('accountingbuddy:thanks'))
	else:
		form = BusinessRequestForm(request=request)
	return render(request, 'business_request_form.html', {'form': form})




  
