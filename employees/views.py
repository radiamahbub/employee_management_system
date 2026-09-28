from django.shortcuts import render, redirect

# Create your views here.
def employee_create(request):

    return render(request, 'employee_create.html')

def employee_view(request):
    
    return render(request, 'employee_view.html')

def employee_update(request):
    
    return render(request, 'employee_update.html')

def employee_delete(request):
    
    return render(request, 'employee_delete.html')