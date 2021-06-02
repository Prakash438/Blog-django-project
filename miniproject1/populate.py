import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','miniproject1.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import * 
faker = Faker()
# digits='0123456789'

def populate(n):
    for i in range(n):
        ferollno = randint(100,999)
        feage = randint(10,60)
        fename = faker.name()
        femno = randrange(6,10)
        for i in range(9):
            femno = str(femno)+str(randrange(0,10))
        feemail = fename+'@gmail.com'
        emp_record = student.objects.get_or_create(roll_no=ferollno,name=fename,age=feage,mobile_no=femno,Email=feemail)
populate(30)
