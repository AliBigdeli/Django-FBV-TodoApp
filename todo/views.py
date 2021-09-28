from django.shortcuts import render, redirect, get_object_or_404

from .models import Task
from .forms import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def index(request):
    tasks = Task.objects.filter(user=request.user)

    form = TaskForm()

    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
        return redirect("/")

    context = {"tasks": tasks, "form": form}
    return render(request, "tasks/list_task.html", context)


@login_required
def updateTask(request, pk):
    task = Task.objects.get(id=pk, user=request.user)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = User.objects.get(pk=request.user.id)
            obj.save()
            return redirect("/")

    context = {"form": form}

    return render(request, "tasks/update_task.html", context)


@login_required
def completeTask(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.complete = True
    item.save()
    return redirect("/")


@login_required
def deleteTask(request, pk):
    item = get_object_or_404(Task, id=pk, user=request.user)
    item.delete()
    return redirect("/")
