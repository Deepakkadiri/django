from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def PaymentReceipt(request):
    return render(request,'Payments/Payment.html')

@login_required
def Invoice(request):
    return render(request,'Payments/Invoice.html')