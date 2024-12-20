from django.shortcuts import render

# Create your views here.
def Gmail(request):
    return render(request,'Credentials/Gmail.html')

def MSTeams(request):
    return render(request,'Credentials/MSTeams.html')

def CodeTantra(request):
    return render(request,'Credentials/CodeTantra.html')