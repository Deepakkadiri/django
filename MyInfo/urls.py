from django.urls import path
from MyInfo.views import Attendance, Profile,CoursePage,MyCredits,AdmissionLetter,Attendance

urlpatterns=[
    path('adletter',AdmissionLetter),
    path('Profile',Profile),
    path('CoursePage',CoursePage),
    path('Credits',MyCredits),
    path('Attendance',Attendance),
]