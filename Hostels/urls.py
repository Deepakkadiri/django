from django.urls import path
from Hostels.views import *

urlpatterns = [
    path('Registration',Registration),
    path('ProvisionalAllotmentletter',ProvisionalAllotmentletter)
]