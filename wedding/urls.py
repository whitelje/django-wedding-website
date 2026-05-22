from django.urls import re_path
from django_distill import distill_re_path

from . import views

urlpatterns = [
#    re_path(r'^$', views.home, name='home'),
    distill_re_path(r'^$', views.home, name='home'),
]
