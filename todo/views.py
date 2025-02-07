from django.shortcuts import redirect, render
from .models import Task

# Create your views here.
def home(request):
    not_complete = Task.objects.filter(is_completed=False).order_by('-updated_at')
    complete = Task.objects.filter(is_completed=True)
    context = {
        'not_complete': not_complete,
        'complete': complete,
    }
    return render(request, 'home.html', context)

def addTask(request):
    add_task = request.POST['task']
    Task.objects.create(task=add_task)
    return redirect('home')
    
    