from django.shortcuts import render,HttpResponse
from .models import Employee,Department,Role
from datetime import datetime
from django.db.models import Q


def index(request):
    return render(request,'emp_app/index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    print(context)
    return render(request,'emp_app/all_emp.html',context)
    

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone=int(request.POST['phone'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
      
        new_emp=Employee(first_name=first_name ,last_name=last_name,phone=phone,salary=salary,bonus=bonus
                 ,dept_id=dept,role_id=role,hire_date=datetime.now())
        new_emp.save()
    
        return HttpResponse('Employee added successfully')
    elif request.method=='GET':
        return render(request,'emp_app/add_emp.html')
    else:
        return HttpResponse('An exception occurred: emp is not added')
def remo_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return HttpResponse("employee removed successfully")
        except:
            return HttpResponse("Please enter valid id")
    emps=Employee.objects.all()
    context={
        "emps":emps
    }
    return render(request,'emp_app/remo_emp.html',context)

def fi_emp(request):
    if request.method=='POST':
        name = request.POST.get('name', '')  # Using .get() to avoid KeyError
        dept = request.POST.get('dept', '')  
        role = request.POST.get('role', '')
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)|Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        return render(request,'emp_app/all_emp.html',context)
    elif request.method=='GET':
        return render(request,'emp_app/fi_emp.html')
    else:
        return HttpResponse("an exception occurred")
