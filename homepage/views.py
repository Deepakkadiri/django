from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def homePage(request):
    return render(request,'index.html')

@login_required
def dash(request):
    return render(request,'dashboard.html')

@login_required
def dash2(request):
    return render(request,'dashboard2.html')


def logoutUser(request):
    return render(request,'registration/Logout.html')