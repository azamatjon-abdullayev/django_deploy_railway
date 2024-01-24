from django.contrib import admin
from myfiles.models import Teacher, Fan, Oquvchi
# Register your models here.

class AdminFan(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Fan,AdminFan)

class AdminTeach(admin.ModelAdmin):
    list_display = ['id','ism','yosh','fan','sana']

admin.site.register(Teacher,AdminTeach)

class AdminOquv(admin.ModelAdmin):
    list_display = ['ism','fam','yosh',]

admin.site.register(Oquvchi,AdminOquv)