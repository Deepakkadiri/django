from django.shortcuts import render

from Examination.models import *
from django.views.generic import *

from django.urls import reverse_lazy

# for Authenciationn
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def ExamsSchedule(request):
    return render(request,'Examination/ExamsSchedule.html')

@login_required
def Results(request):
    result1 = CSEMarks.objects.all()
    result2 = ECEMarks.objects.all()
    result3 = MATMarks.objects.all()
    result4 = ENGMarks.objects.all()
    result5 = PHYMarks.objects.all()

    # <<<---Create dictionary named Dict which contains all the objects of result4,result2,result4,result4,result5  ----->>>>>
    Dict={'result1':result1,'result2':result2,'result3':result3,'result4':result4,'result4':result4,'result5':result5}

    # <<<---returned whole dictionary which contains all the values of result4,result2,result4,result4,result5 ------>>>>>
    return render(request,'Examination/Marks.html',Dict) 

# CSE
@login_required
@permission_required('Examination.view_csemarks')
def ViewCSE(request):
    result1 = CSEMarks.objects.all()
    marks1 = {'result1':result1}
    return render(request,'Examination/CSEMarks.html',marks1)

class AddCSE(CreateView):
    model = CSEMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']

class UpdCSE(UpdateView):
    model = CSEMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']
    template_name_suffix = '_update_form'

class DelCSE(DeleteView):
    model = CSEMarks
    success_url = reverse_lazy('ViewCSE')

# ECE
@login_required
@permission_required('Examination.view_ecemarks')
def ViewECE(request):
    result2 = ECEMarks.objects.all()
    marks2 = {'result2':result2}
    return render(request,'Examination/ECEMarks.html',marks2)

class AddECE(CreateView):
    model = ECEMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']

class UpdECE(UpdateView):
    model = ECEMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']
    template_name_suffix = '_update_form'

class DelECE(DeleteView):
    model = ECEMarks
    success_url = reverse_lazy('ViewECE')

# MAT

@login_required
@permission_required('Examination.view_matmarks')
def ViewMAT(request):
    result3 = MATMarks.objects.all()
    marks3 = {'result3':result3}
    return render(request,'Examination/MATMarks.html',marks3)

class AddMAT(CreateView):
    model = MATMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']

class UpdMAT(UpdateView):
    model = MATMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']
    template_name_suffix = '_update_form'

class DelMAT(DeleteView):
    model = MATMarks
    success_url = reverse_lazy('ViewMAT')

# ENG

@login_required
@permission_required('Examination.view_engmarks')
def ViewENG(request):
    result4 = ENGMarks.objects.all()
    marks4 = {'result4':result4}
    return render(request,'Examination/ENGMarks.html',marks4)

class AddENG(CreateView):
    model = ENGMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']

class UpdENG(UpdateView):
    model = ENGMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']
    template_name_suffix = '_update_form'

class DelENG(DeleteView):
    model = ENGMarks
    success_url = reverse_lazy('ViewENG')

#PHY

@login_required
@permission_required('Examination.view_phymarks')
def ViewPHY(request):
    result5 = PHYMarks.objects.all()
    marks5 = {'result5':result5}
    return render(request,'Examination/PHYMarks.html',marks5)

class AddPHY(CreateView):
    model = PHYMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']

class UpdPHY(UpdateView):
    model = PHYMarks
    fields = ['ExamTitle','MaxMarks','ScoredMarks','Result']
    template_name_suffix = '_update_form'

class DelPHY(DeleteView):
    model = PHYMarks
    success_url = reverse_lazy('ViewPHY')


@login_required
def Marks2(request):
    return render(request,'Examination/Marks2.html') 