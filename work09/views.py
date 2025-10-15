from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from datetime import date


# Create your views here.


def todo_list(request):
    todos = Todo.objects.all().order_by("due_date")
    today = date.today()
    sort_order = request.GET.get("sort", "asc")  # パラメータ sort を取得
    if sort_order == "desc":
        todos = Todo.objects.all().order_by("-due_date")
    else:
        todos = Todo.objects.all().order_by("due_date")

    next_sort = "desc" if sort_order == "asc" else "asc"

    status_filter = request.GET.get("status", "all")

    if status_filter == "completed":
        todos = todos.filter(is_completed=True)
    elif status_filter == "incomplete":
        todos = todos.filter(is_completed=False)

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")
    else:
        form = TodoForm()

    return render(
        request,
        "work09/todo_list.html",
        {
            "todos": todos,
            "form": form,
            "today": today,
            "next_sort": next_sort,
            "sort_order": sort_order,
            "status_filter": status_filter,
        },
    )


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


def todo_edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("work09:todo_list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "work09/todo_edit.html", {"form": form, "todo": todo})


def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed  # ← True/Falseを反転
    todo.save()
    return redirect("work09:todo_list")


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("work09:todo_list")
