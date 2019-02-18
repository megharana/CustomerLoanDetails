from django.db import models
from django.conf import settings


class LoanPart(models.Model):
    mem_id = models.CharField(max_length=10, primary_key=True)
    loan_amnt = models.IntegerField()
    funded_amnt_inv = models.IntegerField()
    term = models.CharField(max_length=20)
    int_rate = models.IntegerField()
    installment = models.IntegerField()
    grade = models.CharField(max_length=1)
    emp_title = models.CharField(max_length=100, null=True, blank=True)
    emp_length = models.CharField(max_length=120)
    home_ownership = models.CharField(max_length=30)
    annual_inc = models.IntegerField()
    verification_status = models.CharField(max_length=20)
    issue_d = models.CharField(max_length=20)
    loan_status = models.CharField(max_length=20)
    desc = models.CharField(max_length=100, null=True, blank=True)
    purpose = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    addr_state = models.CharField(max_length=20)
    last_pymnt_d = models.CharField(max_length=20)
    last_pymnt_amnt = models.CharField(max_length=20)


# class LoanPart_MORTGAGE(models.Model):
#     mem_id = models.CharField(max_length=10, primary_key=True)
#     loan_amnt = models.IntegerField()
#     funded_amnt_inv = models.IntegerField()
#     term = models.CharField(max_length=20)
#     int_rate = models.IntegerField()
#     installment = models.IntegerField()
#     grade = models.CharField(max_length=1)
#     emp_title = models.CharField(max_length=100, null=True, blank=True)
#     emp_length = models.CharField(max_length=120)
#     home_ownership = models.CharField(max_length=30)
#     annual_inc = models.IntegerField()
#     verification_status = models.CharField(max_length=20)
#     issue_d = models.CharField(max_length=20)
#     loan_status = models.CharField(max_length=20)
#     desc = models.CharField(max_length=100, null=True, blank=True)
#     purpose = models.CharField(max_length=20)
#     title = models.CharField(max_length=20)
#     addr_state = models.CharField(max_length=20)
#     last_pymnt_d = models.CharField(max_length=20)
#     last_pymnt_amnt = models.CharField(max_length=20)

# class LoanPart_OWN(models.Model):
#     mem_id = models.CharField(max_length=10, primary_key=True)
#     loan_amnt = models.IntegerField()
#     funded_amnt_inv = models.IntegerField()
#     term = models.CharField(max_length=20)
#     int_rate = models.IntegerField()
#     installment = models.IntegerField()
#     grade = models.CharField(max_length=1)
#     emp_title = models.CharField(max_length=100, null=True, blank=True)
#     emp_length = models.CharField(max_length=120)
#     home_ownership = models.CharField(max_length=30)
#     annual_inc = models.IntegerField()
#     verification_status = models.CharField(max_length=20)
#     issue_d = models.CharField(max_length=20)
#     loan_status = models.CharField(max_length=20)
#     desc = models.CharField(max_length=100, null=True, blank=True)
#     purpose = models.CharField(max_length=20)
#     title = models.CharField(max_length=20)
#     addr_state = models.CharField(max_length=20)
#     last_pymnt_d = models.CharField(max_length=20)
#     last_pymnt_amnt = models.CharField(max_length=20)

# class LoanPart_4yrs(models.Model):
#     mem_id = models.CharField(max_length=10, primary_key=True)
#     loan_amnt = models.IntegerField()
#     funded_amnt_inv = models.IntegerField()
#     term = models.CharField(max_length=20)
#     int_rate = models.IntegerField()
#     installment = models.IntegerField()
#     grade = models.CharField(max_length=1)
#     emp_title = models.CharField(max_length=100, null=True, blank=True)
#     emp_length = models.CharField(max_length=120)
#     home_ownership = models.CharField(max_length=30)
#     annual_inc = models.IntegerField()
#     verification_status = models.CharField(max_length=20)
#     issue_d = models.CharField(max_length=20)
#     loan_status = models.CharField(max_length=20)
#     desc = models.CharField(max_length=100, null=True, blank=True)
#     purpose = models.CharField(max_length=20)
#     title = models.CharField(max_length=20)
#     addr_state = models.CharField(max_length=20)
#     last_pymnt_d = models.CharField(max_length=20)
#     last_pymnt_amnt = models.CharField(max_length=20)

# class LoanPart_5yrs(models.Model):
#     mem_id = models.CharField(max_length=10, primary_key=True)
#     loan_amnt = models.IntegerField()
#     funded_amnt_inv = models.IntegerField()
#     term = models.CharField(max_length=20)
#     int_rate = models.IntegerField()
#     installment = models.IntegerField()
#     grade = models.CharField(max_length=1)
#     emp_title = models.CharField(max_length=100, null=True, blank=True)
#     emp_length = models.CharField(max_length=120)
#     home_ownership = models.CharField(max_length=30)
#     annual_inc = models.IntegerField()
#     verification_status = models.CharField(max_length=20)
#     issue_d = models.CharField(max_length=20)
#     loan_status = models.CharField(max_length=20)
#     desc = models.CharField(max_length=100, null=True, blank=True)
#     purpose = models.CharField(max_length=20)
#     title = models.CharField(max_length=20)
#     addr_state = models.CharField(max_length=20)
#     last_pymnt_d = models.CharField(max_length=20)
#     last_pymnt_amnt = models.CharField(max_length=20)
