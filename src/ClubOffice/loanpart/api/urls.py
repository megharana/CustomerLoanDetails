from django.contrib import admin
from django.urls import path
from loanpart.views import showCustomerName

app_name = 'loanpart'  #necessary to give when including app's url in project's url
urlpatterns = [
    path('member/', showCustomerName, name='Search-member'),
]
