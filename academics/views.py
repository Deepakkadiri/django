from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Facultyinfo(request):
    return render(request,'academics/Facultyinfo.html')

@login_required
def timetable(request):
    return render(request,'academics/timetable.html')