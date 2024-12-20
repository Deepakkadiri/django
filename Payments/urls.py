from django.urls import path
from Payments.views import *

urlpatterns = [
    path('Payment',PaymentReceipt),
    path('Invoice',Invoice)
]