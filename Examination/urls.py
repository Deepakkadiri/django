from django.urls import path
from Examination.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    path('ExamsSchedule',ExamsSchedule),

    path('Results',Results,name="Result"),

    path('ViewCSE',ViewCSE,name="ViewCSE"),
    path('AddCSE',login_required(AddCSE.as_view())),
    path('UpdCSE/<int:pk>/',login_required(UpdCSE.as_view())),
    path('DelCSE/<int:pk>/',login_required(DelCSE.as_view())),

    path('ViewECE',ViewECE,name="ViewECE"),
    path('AddECE',login_required(AddECE.as_view())),
    path('UpdECE/<int:pk>/',login_required(UpdECE.as_view())),
    path('DelECE/<int:pk>/',login_required(DelECE.as_view())),

    path('ViewMAT',ViewMAT,name="ViewMAT"),
    path('AddMAT',login_required(AddMAT.as_view())),
    path('UpdMAT/<int:pk>/',login_required(UpdMAT.as_view())),
    path('DelMAT/<int:pk>/',login_required(DelMAT.as_view())),

    path('ViewENG',ViewENG,name="ViewENG"),
    path('AddENG',login_required(AddENG.as_view())),
    path('UpdENG/<int:pk>/',login_required(UpdENG.as_view())),
    path('DelENG/<int:pk>/',login_required(DelENG.as_view())),

    path('ViewPHY',ViewPHY,name="ViewPHY"),
    path('AddPHY',login_required(AddPHY.as_view())),
    path('UpdPHY/<int:pk>/',login_required(UpdPHY.as_view())),
    path('DelPHY/<int:pk>/',login_required(DelPHY.as_view())),

    path('Marks2',Marks2)
]
