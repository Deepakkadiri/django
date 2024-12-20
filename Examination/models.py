from django.db import models
from django.urls import reverse
# Create your models here.
class CSEMarks(models.Model):
    ExamTitle     = models.CharField(max_length=95)
    MaxMarks      = models.IntegerField()
    ScoredMarks   = models.IntegerField()
    Result        = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse("ViewCSE")

class ECEMarks(models.Model):
    ExamTitle     = models.CharField(max_length=95)
    MaxMarks      = models.IntegerField()
    ScoredMarks   = models.IntegerField()
    Result        = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse("ViewECE")

class MATMarks(models.Model):
    ExamTitle     = models.CharField(max_length=95)
    MaxMarks      = models.IntegerField()
    ScoredMarks   = models.IntegerField()
    Result        = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse("ViewMAT")

class ENGMarks(models.Model):
    ExamTitle     = models.CharField(max_length=95)
    MaxMarks      = models.IntegerField()
    ScoredMarks   = models.IntegerField()
    Result        = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse("ViewENG")

class PHYMarks(models.Model):
    ExamTitle     = models.CharField(max_length=95)
    MaxMarks      = models.IntegerField()
    ScoredMarks   = models.IntegerField()
    Result        = models.CharField(max_length=15)

    def get_absolute_url(self):
        return reverse("ViewPHY")