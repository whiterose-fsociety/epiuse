from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_num = models.IntegerField(primary_key=True,null=False)
    emp_relation = models.ForeignKey('self', verbose_name=("relation"), on_delete=models.CASCADE,null=True,blank=True,related_name="underlings")
    emp_role = models.CharField(max_length=50)
    emp_name = models.CharField(max_length=50)
    emp_surname = models.CharField(max_length=50)
    emp_dob =  models.DateField()
    emp_salary = models.FloatField()

    def __str__(self):
        return f'Employee ID: {self.emp_num} - {self.emp_name} {self.emp_surname} is Epiuse\'s {self.emp_role}'




