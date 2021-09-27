from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="task_list"),
    path("update/<str:pk>/", views.updateTask, name="update_task"),
    path("complete/<str:pk>/", views.completeTask, name="complete_task"),
    path("delete/<str:pk>/", views.deleteTask, name="delete_task"),
]
