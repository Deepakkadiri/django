from django.db import models
from django.urls import reverse
# Create your models here.
class Course(models.Model):
    ClassNbr        = models.IntegerField()
    CourseCode      = models.CharField(max_length=95)
    CourseTitle     = models.CharField(max_length=95)
    CourseType      = models.CharField(max_length=95)
    CourseSystem    = models.CharField(max_length=95)
    Faculty         = models.CharField(max_length=95)
    Slot            = models.CharField(max_length=95)
    CourseMode      = models.CharField(max_length=95)

    def get_absolute_url(self):
        return reverse("ViewCourses")