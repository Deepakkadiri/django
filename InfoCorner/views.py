from django.shortcuts import render


# Create your views here.
def ViewCirculars(request):
    return render(request,'InfoCorner/Circulars.html')

def FAQ(request):
    return render(request,'InfoCorner/FAQ.html')