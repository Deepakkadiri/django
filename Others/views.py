from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def eco(request):
    return render(request,'Others/eco.html')

@login_required
def lac(request):
    return render(request,'Others/lac.html')

@login_required
def naac(request):
    return render(request,'Others/naac.html')

@login_required
def nba(request):
    return render(request,'Others/nba.html')

@login_required
def snptel(request):
    return render(request,'Others/snpetl.html')

