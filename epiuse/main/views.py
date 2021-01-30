from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.urls import reverse
from django.core import serializers
from django.db.models import Count
import json
from .models import *
# Create your views here.
def home(request):
    group = Employee.objects.values("emp_role").annotate(dcount=Count("emp_role"))
    # Result: <QuerySet [{'emp_role': 'Employee', 'dcount': 4}, {'emp_role': 'Manager', 'dcount': 3}, {'emp_role': 'Trainee', 'dcount': 3}]>
    context = {
        "employees":Employee.objects.all().order_by("-emp_salary"),
        "group":group,
    }
    return render(request,"epiuse/home.html",context)

"""
This page has specific information for an individual employee
"""
def employee(request,emp_num):
    try:
        employee = Employee.objects.get(pk=emp_num)
    except Employee.DoesNotExist:
        raise Http404("Employee Does Not Exist")
    if employee.emp_relation_id == None:
            supervisor = Employee.objects.get(pk=employee.emp_num)
    else:
            supervisor = Employee.objects.get(pk = employee.emp_relation_id)
    context = {
        "employee":employee,
        "underlings":employee.underlings.all(),
        "supervisor":supervisor,
    }
    return render(request,"epiuse/employee.html",context)


# AJAX Methods
"""
Here we are abstracting the search function.
JS sends a request to the Python Server and this function will perform a search and return a response to JS. 
request = Date
"""
def search_query(request):
    data = json.loads(request.body)
    dob = data['emp_dob']
    employees = Employee.objects.filter(emp_dob__gte=dob).order_by("emp_num")
    if len(employees) > 0 :
        data = serializers.serialize('json',employees)
    else:
        data = serializers.serialize('json',{})
    print(employees)    
    # context = {
    #     "employees":employees
    # }
    return HttpResponse(data,content_type="application/json")
    # return render(request,"epiuse/home.html",context)

"""
Here we are abstracting the search function.
JS sends a request to the Python Server and this function will perform a search and return a response to JS. 
request = Name or Last Name
"""
def search_name(request):
    data = json.loads(request.body)
    name = data['name']
    print(name)
    if len(Employee.objects.filter(emp_name=name)) > 0:
        employees = Employee.objects.filter(emp_name=name)
        data = serializers.serialize('json',employees)
    elif len(Employee.objects.filter(emp_surname=name)) > 0:
        employees = Employee.objects.filter(emp_surname=name)
        data = serializers.serialize('json',employees)
    else:
        employees = []
        data = serializers.serialize('json',[])
    print(employees)
    return HttpResponse(data,content_type="application/json")

def supervisor(request,emp_num):
    pass
# path("",views.home,name="home"),
#     path('<int:emp_num>',views.employee,name="employee"),
#     path('<int:emp_num>/supervisor',views.supervisor,name='supervisor')
