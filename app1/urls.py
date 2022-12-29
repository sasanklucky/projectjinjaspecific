from django.urls import path
from app1.views import *
app_name='sasank'

urlpatterns=[
    path('jinja_a1/',jinja_a1,name='jinja_a1.html'),
]