from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.views.static import serve


app_name='accountingbuddy'
urlpatterns=[  
url(r'^pricing/india/$',views.pricing_india,name='pricing-india'),
url(r'^businessrequest/submit/$',views.businessFormCreateView.as_view(),name='business-req'),
]
