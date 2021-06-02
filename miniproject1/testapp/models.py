from django.db import models

class CustomManager1(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('age')

    def get_emp_roll_no_range(self,roll1,roll2):
        return super().get_queryset().filter(roll_no__range=(roll1,roll2))
    

class CustomManager2(models.Manager):
    def get_queryset(self):
        return super().get_queryset().order_by('name')

class student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    mobile_no = models.IntegerField()
    Email = models.EmailField()
    roll_no = models.IntegerField()
    objects = CustomManager1()


class Proxystudent(student):
    object = CustomManager2()
    class Meta:
        proxy = True

# Create your models here.
