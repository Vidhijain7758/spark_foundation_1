from django.conf.urls import url,include

from . import views
from rest_framework import routers
from accounts.views import *




urlpatterns = [
    url(r'^register/$', UserCreate, name='account-create'),
    url(r'^register/(?P<id>\d+)/$', user_details, name='account-create1'),
    url(r'^register/$', UserCreationView.as_view()),
]
