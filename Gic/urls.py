from django.urls import path
from Gic.views import *

urlpatterns = [
    path('fe',FeedbackForm),
    path('me',Mentor),
]