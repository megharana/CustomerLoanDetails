from django.contrib import admin
from django.urls import path
from loanpart import .views
urlpatterns = [
    path('member/', views.showCustomerName, name='Search-member'),
]
