from django.conf.urls import url
from django.contrib import admin
from editdistances import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
]
