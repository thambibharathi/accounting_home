from django.views.generic.edit import UpdateView , CreateView, DeleteView
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

from business.models import Business

class BusinessCreate(CreateView):
  model=Business
  template_name="form.html"
  fields=['name']
  
  def get_context_data(self,**kwargs):
    context=super(BusinessCreate,self).get_context_data(**kwargs)
    context['page.form.button_text']='Submit'
    return context
      
  
