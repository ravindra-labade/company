from django.db import models


class Company(models.Model):
    company_name = models.CharField(max_length=20)
    company_address = models.CharField(max_length=20)
    about_company = models.CharField(max_length=50)
    number_of_employee = models.IntegerField()
    company_ceo = models.CharField(max_length=20)
    choice = [('WFH', 'Work From Home'), ('WFO', 'Work From Office')]
    work_mode = models.CharField(max_length=10, choices=choice)

