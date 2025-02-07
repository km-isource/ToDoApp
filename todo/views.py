from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task

# Create your views here.
def home(request):
    complete = Task.objects.filter(is_completed=True).order_by('-updated_at')
    not_complete = Task.objects.filter(is_completed=False).order_by('-updated_at')
    context = {
        'complete': complete,
        'not_complete': not_complete,
    }
    return render(request, 'home.html', context)

def add_task(request):
    add_task = request.POST.get('task')
    Task.objects.create(task=add_task)
    return redirect('home')


def mark_as_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

def mark_as_not_done(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

def edit_task(request, pk):
    if request.method == "POST":
        task = get_object_or_404(Task, pk=pk)
        new_task_value = request.POST.get("task")
        task.task = new_task_value
        task.save()
        return JsonResponse({"status": "success", "task": task.task})
    return JsonResponse({"status": "error"})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home')

