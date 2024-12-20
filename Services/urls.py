from django.urls import path
from Services.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('TransportRegistration',TransportRegistration),
    path('ViewCourses',CoursesList,name="ViewCourseslist"),
    path('AddCourse',login_required(AddCourse.as_view())),
    path('UpdCourse/<int:pk>/',login_required(UpdCourse.as_view())),
    path('DelCourse/<int:pk>/',login_required(DelCourse.as_view())),
    path('ViewCourses2',Course2,name="ViewCourses"),
]