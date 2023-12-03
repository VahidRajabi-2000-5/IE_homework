from django.urls import path

from . import views


urlpatterns = [
    # path('',views.task_list,name='task_list'),
    # path('<int:pk>/',views.task_detail,name='task_detail'),
    path('',views.TaskListView.as_view(),name='task_list'),
    path('<int:pk>/',views.TaskDetailView.as_view(),name='task_detail'),
    path('create/',views.CreateTaskView.as_view(),name='task_create'),
    path('update/<int:pk>/',views.UpdateTaskView.as_view(),name='task_update'),
    path('delete/<int:pk>/',views.DeleteTaskView.as_view(),name='task_delete'),
    path('command/<int:pk>/',views.CommandCreateView.as_view(),name='command_create'),
    
    
]
