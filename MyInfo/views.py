from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def AdmissionLetter(request):
    return render(request,'MyInfo/ALLOTMENT.html')

@login_required
def Profile(request):
    return render(request,'MyInfo/Profile.html')

@login_required
def CoursePage(request):
    return render(request,'MyInfo/CoursePage.html')

@login_required
def MyCredits(request):
    return render(request,'MyInfo/Credits.html')

@login_required
def Attendance(request):
    return render(request,'MyInfo/Attendance.html')
