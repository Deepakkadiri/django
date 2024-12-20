from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def MyResearchProfile(request):
    return render(request,'Research/MyResearchProfile.html')

@login_required
def MyResearchProfile2(request):
    return render(request,'Research/Profile.html')

@login_required
def funding(request):
    return render(request,'Research/funding.html')