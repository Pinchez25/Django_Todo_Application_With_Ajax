from django.urls import path
from .views import TodoDetail,CreateTodo,UpdateTodo,completeTodo,searchTodo,getTodos,HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='todos'),
    path('todo/<str:pk>/', TodoDetail.as_view(), name='todo-detail'),
    path('create-todo/',CreateTodo.as_view(), name='create-todo'),
    path('update-todo/<str:pk>/',UpdateTodo.as_view(), name='update-todo'),
    path('complete_todo/',completeTodo),
    path('search/',searchTodo),
    path('todos/',getTodos),
]
