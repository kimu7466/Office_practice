from django.urls import path
from .views import *


urlpatterns = [
    path("", home_view, name='home_view'),

    path("departments", dept_view, name='dept_view'),
    path("add_dept", add_dept, name='add_dept'),
    path("edit_dept/<int:id>", edit_dept, name='edit_dept'),
    path("delete_dept/<int:id>", delete_dept, name='delete_dept'),

    path("employees", emp_view, name='emp_view'),
    path("add_emps", add_emps, name='add_emps'),
    path("edit_emp/<int:id>", edit_emp, name='edit_emp'),
    path("delete_emp/<int:id>", delete_emp, name='delete_emp'),

    path('deptAPI',deptAPI, name='deptAPI' ),
    path('depDetailAPI/<int:id>',depDetailAPI, name='depDetailAPI' ),

    path('empAPI',empAPI, name='empAPI' ),
    
    # path('empDetailAPI/<int:id>', empDetailAPI, name='empDetailAPI' ),


    # path('EmployeeAPIView',EmployeeAPIView.as_view(), name='EmployeeAPIView' ),
]