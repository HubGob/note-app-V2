from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {"tasks": tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        note = request.POST.get('note')
        if title:  # Note can be optional
            Task.objects.create(title=title, note=note)  # Create ONE task with both fields
            return redirect('task_list')
    return render(request, 'todo/add_task_form.html')

def update_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        note = request.POST.get('note')
        if title:  # Note can be optional
            task.title = title  # Update existing task
            task.note = note
            task.save()
            return redirect('task_list')
    return render(request, 'todo/update_task_form.html', {'task': task})  # Pass task to template

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('task_list')
    return render(request, 'todo/confirm_delete_form.html', {'task': task})  # Pass task to template