from django.contrib import admin
from .models import  Business

# Register your models here.


class BusinessAdmin(admin.ModelAdmin):
  list_display=('id','name','code','user','created')
  list_filter=('id','name','code','user','created')
  search_fields=('name','code','user','created')
  ordering=('name')
  
  

admin.site.register(Business,BusinessAdmin)

