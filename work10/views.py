from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm
from datetime import date
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.


@login_required  # ここでログイン必須にする
def todo_list(request):
    todos = Todo.objects.filter(user=request.user)  # 自分のタスクだけ取得
    today = timezone.now().date()

    sort_order = request.GET.get("sort", "asc")
    if sort_order == "desc":
        todos = todos.order_by("-due_date")
    else:
        todos = todos.order_by("due_date")

    next_sort = "desc" if sort_order == "asc" else "asc"
    status_filter = request.GET.get("status", "all")
    if status_filter == "completed":
        todos = todos.filter(is_completed=True)
    elif status_filter == "incomplete":
        todos = todos.filter(is_completed=False)

    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user  # ←必須
            todo.save()
            return redirect("work10:todo_list")
        else:
            print(form.errors)
    else:
        form = TodoForm()

    return render(
        request,
        "work10/todo_list.html",
        {
            "todos": todos,
            "form": form,
            "today": today,
            "next_sort": next_sort,
            "sort_order": sort_order,
            "status_filter": status_filter,
        },
    )


@login_required
def todo_create(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect("work10:todo_list")
        else:
            print(form.errors)
    else:
        form = TodoForm()
    return render(request, "work10/todo_create.html", {"form": form})


def todo_edit(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("work10:todo_list")
    else:
        form = TodoForm(instance=todo)
    return render(request, "work10/todo_edit.html", {"form": form, "todo": todo})


def todo_toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.is_completed = not todo.is_completed  # ← True/Falseを反転
    todo.save()
    return redirect("work10:todo_list")


def todo_delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.delete()
    return redirect("work10:todo_list")


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("todo_list")
    else:
        form = UserCreationForm()

    return render(request, "work10/register.html", {"form": form})


# ログインしてタスクを作成できるところまで次は、誰がそのタスクを作成したか表示
