from django.urls import path
from Others.views import *

urlpatterns = [
    path('eco',eco),
    path('lac',lac),
    path('naac',naac),
    path('nba',nba),
    path('snpetl',snptel),
]