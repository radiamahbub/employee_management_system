from django.urls import path
from employees.views import *

urlpatterns = [
    path('employee/', employee_create, name='employee_create'),
    path('employee_view/', employee_view, name='employee_view'),
    path('employee_update/', employee_update, name='employee_update'),
    path('employee_delete/', employee_delete, name='employee_delete'),
]