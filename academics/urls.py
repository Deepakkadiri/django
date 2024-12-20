from django.urls import path
from academics.views import Facultyinfo,timetable

urlpatterns=[
    path('Facultyinfo',Facultyinfo),
    path('timetable',timetable),
]