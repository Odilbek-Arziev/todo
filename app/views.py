from django.shortcuts import render, redirect
from .models import Todo


def home(request):
    todos = Todo.objects.all()
    new_todo = request.POST.get("todo")
    todo_pk = request.GET.get("todo")

    if todo_pk:
        todo = todos.get(pk=todo_pk)
        todo.is_done = False if todo.is_done else True
        todo.save()

        return redirect("app:home")

    if request.method == "POST" and new_todo:
        Todo.objects.create(text=new_todo, is_done=False)
        return redirect("app:home")

    statistics = {
        "all": todos.count(),
        "finished": todos.filter(is_done=True).count(),
        "open": todos.filter(is_done=False).count(),
    }

    context = {"todos": todos, "stat": statistics}
    return render(request, "home.html", context)


def delete_todo(request, pk):
    if request.method == "POST":
        todo = Todo.objects.get(pk=pk)
        todo.delete()
        return redirect("app:home")

    return render(request, "delete_todo.html", {})


def edit_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == "POST":
        todo.text = request.POST.get("todo")
        todo.save()
        return redirect("app:home")
    return render(request, "edit_todo.html", {"todo": todo})
