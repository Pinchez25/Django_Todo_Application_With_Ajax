from .models import Todo
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView
from .forms import TodoForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse as jr
from django.db.models import Q
from django.views.generic import TemplateView
from datetime import datetime as dt
import humanize as h


class HomeView(TemplateView):
    template_name: str = "todos/index.html"

# class TodosList(ListView):
#     model = Todo
#     template_name = "todos/index.html"
#     context_object_name= "todos"
#     def get_queryset(self):
#         return Todo.objects.filter(complete=False)
    
class TodoDetail(DetailView):
    model = Todo
    context_object_name = "todo"
    template_name: str  = "todos/todo.html"
    
class CreateTodo(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = '/'
    template_name: str= "todos/create-todo.html"
    
class UpdateTodo(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = '/'
    template_name: str= "todos/create-todo.html"
    
def getTodos(request):
    todos = []
    if request.method=="GET":
        results = Todo.objects.filter(complete=False)
        
        for result in results:
            time = result.created.replace(tzinfo=None)
            now = dt.now().replace(tzinfo=None)
            delta = now-time
        
            todos.append({
                "id":result.pk,
                "title":result.title,
                "body":result.body,
                "created":h.naturaltime(delta),
        
            })
    return jr({
        "todos":todos
    })
        
        
    
def completeTodo(request):
    if request.method=="POST":
        todo_id = int(request.POST.get('todo_id'))
        todo = get_object_or_404(Todo, pk=todo_id)
        todo.complete=True
        todo.save()
    return jr({
        'complete':True
    }, safe=False)
    
def searchTodo(request):
    todo=[]
    
    if request.method=="GET":
        search_query = request.GET.get("todo")
        results = Todo.objects.filter(
            (
               Q(title__icontains=search_query) | 
               Q(body__icontains=search_query)
            ) & Q(complete__exact=False)
            )
        for result in results:
            todo.append({
                "id":result.pk,
                "title":result.title,
                "body":result.body,
                "created":result.created,
            })    
    return jr({
        "todo_search":todo
    },safe=False)
 
        
        
    
    


