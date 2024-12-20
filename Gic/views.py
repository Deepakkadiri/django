from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def FeedbackForm(request):
    return render(request,'Gic/feedback.html')

@login_required
def Mentor(request):
    return render(request,'Gic/Mentor.html')