from django.urls import path
from specific.views import *
app_name='specific'

urlpatterns=[
     
     path('kalayan/',kalayan,name='kalayan'),
    path('nvn/',nvn,name='nvn'),

]