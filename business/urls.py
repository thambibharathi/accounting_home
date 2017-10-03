from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.views.static import serve
from django.views.generic import TemplateView


app_name='business'
urlpatterns=[  
url(r'^business/create/$',views.BusinessCreateView,name='business-create'),
]
