from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Registration(request):
    return render(request,'Hostels/HostelRegistration.html')

@login_required
def ProvisionalAllotmentletter(request):
    return render(request,'Hostels/ProvisionalAllotmentletter.html')