from django.shortcuts import render
from django.http import HttpResponse

from django.db import connections

import MySQLdb

# db_conn = connections['default']
db_conn = MySQLdb.connect(
    host='localhost',
    database='ClubOffice',
    user='root',
    password='ShowMe@Pwd123')


# Create your views here.
def showCustomerName(request):
    sql_select_Query = "select emp_title from ClubOffice.Cust_LoanDetails where member_id = '1311748' "

    cursor = db_conn.cursor()

    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print(records)
