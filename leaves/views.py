from django.shortcuts import render, redirect

# Create your views here.
def leave_create(request):

    return render(request, 'leave_create.html')

def leave_view(request):
    
    return render(request, 'leave_view.html')

def leave_update(request):
    
    return render(request, 'leave_update.html')

def leave_delete(request):
    
    return render(request, 'leave_delete.html')