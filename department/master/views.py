from django.shortcuts import render, redirect
from .models import Departments, Employee
from .serializers import DepartmentSerializers, EmployeeSerializers
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import os
from datetime import timedelta
from django.utils import timezone
from django.conf import settings



def home_view(request):
    return render (request, "master/home.html")

def dept_view(request):
    get_dept = Departments.objects.all()
    context = {"depts":get_dept}
    return render (request, "master/departments.html", context=context)

def add_dept(request):
    if request.method == "POST":
        name_ = request.POST["name"]
        about_ = request.POST["about"]
        Departments.objects.create(d_name=name_, about = about_)
        return redirect(dept_view)
    return render(request, "master/add_dept.html")

def edit_dept(request,id):
    dep = Departments.objects.get(id=id)
    if request.method == "POST":
        name_ = request.POST["name"]
        about_ = request.POST["about"]

        dep.d_name = name_
        dep.about = about_
        dep.save()

        return redirect(dept_view)

    return render (request, "master/add_dept.html", {
    "dep":dep,
    "is_edit":True
    })

def delete_dept(request, id):
    dep = Departments.objects.get(id=id)
    dep.delete()
    return redirect(dept_view)

def emp_view(request):
    
    # mytime = timezone.now()   
    # print(mytime)

    get_emps = Employee.objects.all()
    context = {"emps":get_emps}
    return render (request, "master/employees.html", context=context)

def add_emps(request):
    dept = Departments.objects.all()
    if request.method == "POST":
        dept_ = request.POST["dept"]
        name_ = request.POST["name"]
        password_ = request.POST["password"]

        if "profile" in request.FILES:
            profile_ = request.FILES["profile"]
            Employee.objects.create(dept_id=dept_, name = name_ , password = password_, profile = profile_ )

        else:
            Employee.objects.create(dept_id=dept_, name = name_ , password = password_ )
            
        return redirect(emp_view)

    return render(request, "master/add_emps.html",{"dept":dept})

def edit_emp(request, id):
    emp = Employee.objects.get(id=id)
    dept = Departments.objects.all()
    
    if request.method == "POST":
        id_ = request.POST["id"]
        dept_ = request.POST["dept"]
        name_ = request.POST["name"]
        password_ = request.POST["password"]

        if "profile" in request.FILES:
            profile_ = request.FILES["profile"]
            
            # Check if the employee already has a profile image and delete it
            if emp.profile:
                # Delete the old profile image from the filesystem
                old_image_path = emp.profile.path
                if os.path.isfile(old_image_path):
                    os.remove(old_image_path)
            
            # Assign the new profile image
            emp.profile = profile_

        emp.id = id_
        emp.dept_id = dept_
        emp.name = name_
        emp.password = password_
        emp.save()
        
        return redirect(emp_view)
    
    context = {
        "emp": emp,
        "dept": dept,
        "is_edit": True
    }
    
    return render(request, "master/add_emps.html", context)

def delete_emp(request, id):
    emp = Employee.objects.get(id=id)

    # Check if the employee has a profile image and delete it
    if emp.profile:
        old_image_path = emp.profile.path
        if os.path.isfile(old_image_path):
            os.remove(old_image_path)

    # Delete the employee record
    emp.delete()

    return redirect(emp_view)












@api_view(['GET', 'POST'])
def deptAPI(request):
    if request.method == 'GET':
        queryset = Departments.objects.all()
        serializer = DepartmentSerializers(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = DepartmentSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def depDetailAPI(request,id):
    try:
        queryset = Departments.objects.get(id=id)
    except Exception as e:
        return Response({"message":e}, status= status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializier = DepartmentSerializers(queryset)
        return Response(serializier.data, status = status.HTTP_200_OK)

    if request.method == "PUT":
        serializier = DepartmentSerializers(queryset, data= request.data)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data, status=status.HTTP_201_CREATED)
        return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "PATCH":
        serializier =DepartmentSerializers(queryset, data=request.data, partial=True)
        if serializier.is_valid():
            serializier.save()
            return Response(serializier.data, status=status.HTTP_201_CREATED)
        return Response(serializier.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST'])
def empAPI(request):
    if request.method == 'GET':
        queryset = Employee.objects.all()
        serializer = EmployeeSerializers(queryset,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = EmployeeSerializers(data=request.data)
        if serializer.is_valid():
            print("Valid serializer")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Serializer errors:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
