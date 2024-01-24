from django.db import models

# Create your models here.
class Fan(models.Model):
    nomi = models.CharField(max_length=50)

    def __str__(self):
        return self.nomi


class Teacher(models.Model):
    ism = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    yosh = models.IntegerField()
    sana = models.DateField()
    fan = models.ForeignKey(Fan,on_delete=models.CASCADE)


class Oquvchi(models.Model):
    ism = models.CharField(max_length=50)
    fam = models.CharField(max_length=50)
    yosh = models.IntegerField()