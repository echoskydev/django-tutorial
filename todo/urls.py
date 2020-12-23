from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='todo_index'),
    path('add', views.addNewTodo, name='todo_add'),
    path('complete/<todo_id>', views.completeTodo, name='todo_complete'),
    path('delete', views.deleteTodo, name='todo_delete'),
]
