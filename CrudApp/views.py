from django.shortcuts import render,redirect
from .models import Employee
from django.http import HttpResponse

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

def deleteEmployee(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/employees-list')

def openEditForm(request,id):
    emp=Employee.objects.get(id=id)
    return render(request,"employee-update-form.html",{'employee':emp})

def updateEmployee(request,id):
    emp=Employee.objects.get(id=id)
    emp.name=request.POST['name']
    emp.phone=request.POST['phone']
    emp.email=request.POST['email']
    emp.salary=request.POST['salary']
    emp.save()
    return redirect('/employees-list')