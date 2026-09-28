from django.urls import path
from leaves.views import *

urlpatterns = [
    path('leave/', leave_create, name='leave_create'),
    path('leave_view/', leave_view, name='leave_view'),
    path('leave_update/', leave_update, name='leave_update'),
    path('leave_delete/', leave_delete, name='leave_delete'),
]