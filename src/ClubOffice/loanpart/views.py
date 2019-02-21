from django.shortcuts import render
from django.http import HttpResponse

from .models import Cust_LoanDetails


# Create your views here.
def showCustomerName(request):
    p = Cust_LoanDetails.objects.values('mem_id')
    print(p)
    return render(request, 'GetUserDetails.html', {'data': p})
