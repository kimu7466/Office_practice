from django.db import models
from django.utils import timezone


class BaseClass(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Departments(BaseClass):
    d_name = models.CharField(max_length=20)
    about = models.TextField(blank=True)

    def __str__(self):
        return f"{self.d_name}"

class Employee(BaseClass):
    profile = models.ImageField(upload_to=r"images/",default=r"default/image.png")
    dept = models.ForeignKey(Departments,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    comp_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.name}"

