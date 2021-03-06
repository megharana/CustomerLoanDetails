from django.core.management.base import BaseCommand, CommandError
from loanpart.models import Cust_LoanDetails
import csv

# from float import float


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('/Users/megharana/Downloads/loan_part_0009b606f.csv',
                  'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            count_own = 0
            for row in csv_reader:
                if count_own > 0:
                    entry = Cust_LoanDetails(
                        mem_id=row[0],
                        loan_amnt=int(row[1]),
                        funded_amnt_inv=(row[2]),
                        term=row[3],
                        int_rate=float(row[4]),
                        installment=float(row[5]),
                        grade=row[6],
                        emp_title=row[7],
                        emp_length=row[8],
                        home_ownership=row[9],
                        annual_inc=float(row[10]),
                        verification_status=row[11],
                        issue_d=row[12],
                        loan_status=row[13],
                        desc=row[14],
                        purpose=row[15],
                        title=row[16],
                        addr_state=row[17],
                        last_pymnt_d=row[18],
                        last_pymnt_amnt=float(row[19]))
                    entry.save()
                count_own += 1
                print(count_own)
            print(count_own)


# import pandas
# import copy
# df = pandas.read_csv(
#     '/Users/megharana/Downloads/loan_part_0009b606f.csv', delimiter=",")

# print(df[df['home_ownership'].str.contains('RENT')])
