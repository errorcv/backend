import datetime

from django.db import models


class JobPosition(models.Model):
    job_title = models.CharField(max_length=100, blank=False)
    category = models.CharField(max_length=200, null=True, blank=True)
    min_salary = models.CharField(max_length=200, null=True, blank=True)
    max_salary = models.CharField(max_length=200, null=True, blank=True)
    position_status = models.CharField(max_length=200, null=True, blank=True)
    description = models.CharField(max_length=200, null=True, blank=True) 
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ['job_title']

    def __str__(self):
        return self.job_title if self.job_title else ''
