# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CustomerLoandetails(models.Model):
    member_id = models.IntegerField(primary_key=True)
    loan_amnt = models.IntegerField(blank=True, null=True)
    funded_amnt_inv = models.IntegerField(blank=True, null=True)
    term = models.TextField(blank=True, null=True)
    int_rate = models.FloatField(blank=True, null=True)
    installment = models.FloatField(blank=True, null=True)
    grade = models.TextField(blank=True, null=True)
    emp_title = models.TextField(blank=True, null=True)
    emp_length = models.TextField(blank=True, null=True)
    home_ownership = models.TextField(blank=True, null=True)
    annual_inc = models.IntegerField(blank=True, null=True)
    verification_status = models.TextField(blank=True, null=True)
    issue_d = models.TextField(blank=True, null=True)
    loan_status = models.TextField(blank=True, null=True)
    desc = models.TextField(blank=True, null=True)
    purpose = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    addr_state = models.TextField(blank=True, null=True)
    last_pymnt_d = models.TextField(blank=True, null=True)
    last_pymnt_amnt = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Customer_LoanDetails'
# Unable to inspect table 'auth_group'
# The error was: (2013, 'Lost connection to MySQL server during query')
# Unable to inspect table 'auth_group_permissions'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'auth_permission'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'auth_user'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'auth_user_groups'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'auth_user_user_permissions'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'django_admin_log'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'django_content_type'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'django_migrations'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'django_session'
# The error was: (2006, 'MySQL server has gone away')
# Unable to inspect table 'loanpart_loanpart'
# The error was: (2006, 'MySQL server has gone away')
