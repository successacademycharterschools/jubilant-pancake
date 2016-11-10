from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from .views import calcDistance


urlpatterns = [
    url(r'^calc/', calcDistance.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
