from django.shortcuts import render,redirect
from .models import Employee

# Create your views here.
def openIndexPage(request):
    return render(request,"index.html")

def openEmployeeForm(request):
    return render(request,"employee-form.html")

def saveEmployee(request):
    emp=Employee()
    emp.name=request.POST['name']
    emp.phone=request.POST['phone']
    emp.email=request.POST['email']
    emp.salary=request.POST['salary']
    emp.save()
    return redirect('/employees-list')

def openEmployeesList(request):
    employeesList=Employee.objects.all()
    return render(request,"employees-list.html",{'employees':employeesList})