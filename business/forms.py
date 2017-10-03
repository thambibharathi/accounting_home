from django import forms
from django.forms import ModelForm 
from django.core.exceptions import ValidationError

from .models import  Business

class BusinessCreateForm(ModelForm):
  class Meta:
    model=Business
    fields=['name']
  def save(self,user):
    bus=super(BusinessCreateForm,self).save(commit=False)
    bus.user=user
    bus.code='code'
    bus.save()
    return bus
    
    '''
    def __init__(self,*args,**kwargs):
      self.request=kwargs.pop('request',None)
      super(BusinessCreateForm,self).__init__(*args,**kwargs)
      self.fields['user']=request.user
      self.fields['code']='code'
      '''
      

