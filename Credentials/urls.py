from django.urls import path
from Credentials.views import *

urlpatterns = [
    path('Gmail',Gmail),
    path('MSTeams',MSTeams),
    path('CodeTantra',CodeTantra),
]