from django.urls import path
from Research.views import *

urlpatterns = [
    path('MyResearchProfile',MyResearchProfile),
    path('MyResearchProfile2',MyResearchProfile2),
    path('funding',funding),
]
