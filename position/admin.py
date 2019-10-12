from django.contrib import admin

from utils.export_csv import ExportCsv
from .models import JobPosition


# Register your models here.
@admin.register(JobPosition)
class JobPositionAdmin(admin.ModelAdmin, ExportCsv):
    list_display = ("job_title", "category", "city")
    actions = ["export_as_csv"]
