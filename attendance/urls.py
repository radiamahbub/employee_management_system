from django.urls import path
from attendance.views import *

urlpatterns = [
    path('attendance/', attendance_create, name='attendance_create'),
    path('attendance_view/', attendance_view, name='attendance_view'),
    path('attendance_update/', attendance_update, name='attendance_update'),
    path('attendance_delete/', attendance_delete, name='attendance_delete'),
]