from django.shortcuts import render
from .models import Todo

def todo_view(request):
    todos = Todo.objects.all() #앞의 Todo를 인폴트? : from .models import Todo
    data = {
        "todos" : todos,
    }

    return render(request, "todo_list.html", data)

def progress_view(request):
    todos = Todo.objects.all() #앞의 Todo를 인폴트? : from .models import Todo
    data = {
        "todos" : todos,
    }

    return render(request, "todo_in_progress.html", data)
# Create your views here.
