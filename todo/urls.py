from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/addtask/', views.addTask, name='add_task' )
]
