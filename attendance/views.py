from django.shortcuts import render, redirect

# Create your views here.
def attendance_create(request):

    return render(request, 'attendance_create.html')

def attendance_view(request):
    
    return render(request, 'attendance_view.html')

def attendance_update(request):
    
    return render(request, 'attendance_update.html')

def attendance_delete(request):
    
    return render(request, 'attendance_delete.html')