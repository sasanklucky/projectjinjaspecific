from django.urls import path
from app2.views import *
app_name='lucky'

urlpatterns=[
    path('jinja_a2/',jinja_a2,name='jinja_a2.html'),
]