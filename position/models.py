import datetime

from django.db import models


class JobPosition(models.Model):
    job_id = models.CharField(max_length=10, unique=True, null=True, blank=True)
    job_title = models.CharField(max_length=100, blank=False)
    location = models.CharField(max_length=100, null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    job_type = models.CharField(max_length=100, null=True, blank=True)
    pub_date = models.DateField('date posted', auto_now=True)
    description = models.CharField(max_length=200, null=True, blank=True) 

    class Meta:
        ordering = ['job_title']

    def __str__(self):
        return self.job_title if self.job_title else ''
