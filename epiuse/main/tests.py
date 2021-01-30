from django.test import TestCase,Client
from .models import *
# Create your tests here.
#emp_num,emp_relation,emp_role,emp_name,emp_surname,emp_dob,emp_salary
class MainTestCase(TestCase):
    def setUp(self):
        #Create Managers
        molefe = Employee.objects.create(emp_num=79,emp_role="Manager",emp_name="Molefe",emp_surname="Molefe",emp_dob="1999-10-21",emp_salary=450000)
        mohapi = Employee.objects.create(emp_num=82,emp_role="Manager",emp_name="Mohapi",emp_surname="Polo",emp_dob="1999-5-15",emp_salary=451120)

        #Create Employees
        rahima = Employee.objects.create(emp_num=45,emp_role="Employee",emp_name="Rahima",emp_surname="Poonyanee",emp_dob="1999-11-08",emp_salary=100000)
        mark = Employee.objects.create(emp_num=452,emp_role="Employee",emp_name="Mark",emp_surname="Nsnis",emp_dob="1999-06-20",emp_salary=120000)
        molefe.underlings.add(rahima)
        molefe.underlings.add(mark)
        
    def test_underling_count(self):
        mo = Employee.objects.get(emp_num=79)
        self.assertEqual(mo.underlings.count(),2)
    # Test If The Index Page Exists
    def test_index(self):
        client = Client()
        response = client.get("/")
        self.assertEqual(response.status_code,200)