from django.urls import path
from accounts.views import *

urlpatterns = [
    path('login/', login_page, name='login'),
    path('register/', register_page, name='register'),
    path('dashboard/', dashboard_page, name='dashboard'),
    path('logout/', logout_page, name='logout'),
]