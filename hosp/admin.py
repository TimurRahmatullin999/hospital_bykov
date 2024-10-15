from django.contrib import admin
from hosp.models import Doctors, Patient, Hospitals, Manager, Record
# Register your models here.

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

@admin.register(Manager)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

@admin.register(Hospitals)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('adress',)

@admin.register(Doctors)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')

@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = ('diagnosis',)