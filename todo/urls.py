from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('todo/add-task/', views.add_task, name='add_task' ),
    path('todo/mark-as-done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    path('todo/undo-task/<int:pk>/', views.mark_as_not_done, name='mark_as_not_done'),
    path('todo/edit-task/<int:pk>/', views.edit_task, name='edit_task'),
    path('todo/delete-task/<int:pk>/', views.delete_task, name='delete_task'),
]
