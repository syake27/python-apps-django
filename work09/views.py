from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


# Create your views here.


def todo_list(request):
    todos = Todo.objects.all().order_by("due_date")

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")
    else:
        form = TodoForm()

    return render(request, "work09/todo_list.html", {"todos": todos, "form": form})


def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")
        else:
            print(form.errors)  # ここでエラー内容を確認
    else:
        form = TodoForm()
    return render(request, "work09/todo_create.html", {"form": form})
