from django.urls import path
from InfoCorner.views import *

urlpatterns = [
    path('ViewCirculars',ViewCirculars),
    path('FAQ',FAQ),
]