from django.shortcuts import render
from myfiles.models import *
from djangofiles.urls import *
# Create your views here.
def home(uy):
    if 'idd' in uy.POST:
        name = uy.POST.get('11')
        last_name = uy.POST.get('22')
        age = uy.POST.get('33')
        id_raqam = uy.POST.get('idd')
        Oquvchi(id=id_raqam,ism=name, fam=last_name, yosh=age).save()

    elif uy.method=="POST":
        name = uy.POST.get('11')
        last_name = uy.POST.get('22')
        age = uy.POST.get('33')
        Oquvchi(ism=name, fam=last_name, yosh=age).save()
    studentlar = Oquvchi.objects.all()
    return render(uy,'index.html',{'talaba':studentlar})
def teacher(malumot):
    return render(malumot,'teacher.html')

def Delete(malumot,id_raqam):
    student = Oquvchi.objects.get(id=id_raqam).delete()
    studentlar = Oquvchi.objects.all()
    return render(malumot,'index.html',{'talaba':studentlar})

def add_oqituvchi(malumot):
    return render(malumot, 'teacher.html')

def update_uchun(malumot, id):
    student = Oquvchi.objects.get(id=id)
    return render(malumot, 'update.html', {'student':student})