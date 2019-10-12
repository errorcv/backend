from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=200, null=True, blank=False)
    company_logo = models.CharField(max_length=200, null=True, blank=True)
    # cb_name = models.CharField(max_length=200, null=True)
    # cb_company_logo = models.CharField(max_length=200, null=True, blank=True)
    # cb_domain = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    county = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zip_code = models.CharField(max_length=200, null=True, blank=True)
    

    class Meta:
        ordering = ['company_name']

    def __str__(self):
        return self.company_name
