from django.contrib import admin
from Examination.models import CSEMarks,ECEMarks,MATMarks,ENGMarks,PHYMarks

# Register your models here.
class CSEMarksAdmin(admin.ModelAdmin):
    list_display=['id','ExamTitle','MaxMarks','ScoredMarks','Result']

admin.site.register(CSEMarks,CSEMarksAdmin)

class ECEMarksAdmin(admin.ModelAdmin):
    list_display=['id','ExamTitle','MaxMarks','ScoredMarks','Result']

admin.site.register(ECEMarks,ECEMarksAdmin)

class MATMarksAdmin(admin.ModelAdmin):
    list_display=['id','ExamTitle','MaxMarks','ScoredMarks','Result']

admin.site.register(MATMarks,MATMarksAdmin)

class ENGMarksAdmin(admin.ModelAdmin):
    list_display=['id','ExamTitle','MaxMarks','ScoredMarks','Result']

admin.site.register(ENGMarks,ENGMarksAdmin)

class PHYMarksAdmin(admin.ModelAdmin):
    list_display=['id','ExamTitle','MaxMarks','ScoredMarks','Result']

admin.site.register(PHYMarks,PHYMarksAdmin)