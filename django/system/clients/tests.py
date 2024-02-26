from django.test import TestCase
import datetime


# Create your tests here.

# VALID DATE
def valid_date(date):

    date_split = str(date).split('-')

    if datetime.date(year=1900, month=1, day=1) < datetime.date(year=int(date_split[0]), month=int(date_split[1]), day=int(date_split[2])) <= datetime.date.today():
        return True

    return False

print(valid_date('1985-11-05'))