from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import *
from Services.models import *

# Create your views here.
@login_required
def TransportRegistration(request):
    return render(request,'Services/TransportRegistration.html')

def CoursesList(request):
    result1 = Course.objects.all()
    marks1 = {'result1':result1}
    return render(request,'Services/Courses.html',marks1)

class AddCourse(CreateView):
    model = Course
    fields = ['ClassNbr','CourseCode','CourseTitle','CourseType','CourseSystem','Faculty','Slot','CourseMode']

class UpdCourse(UpdateView):
    model = Course
    fields = ['ClassNbr','CourseCode','CourseTitle','CourseType','CourseSystem','Faculty','Slot','CourseMode']
    template_name_suffix = '_update_form'

class DelCourse(DeleteView):
    model = Course
    success_url = reverse_lazy('ViewCourses')

def Course2(request):
    result1 = Course.objects.all()
    marks1 = {'result1':result1}
    return render(request,'Services/Courses2.html',marks1)