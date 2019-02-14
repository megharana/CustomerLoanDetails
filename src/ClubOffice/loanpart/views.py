from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def showCustomerName(request):
    html = "<html><body>WORKING</body></html>"
    return HttpResponse(html)