from django.urls import path
from . import views

urlpatterns = [
    path('',views.TaskList, name='tasks'),
    path('task/<int:pk>',views.TaskDetails, name='details'), #<int:pk> used to specify the task object
    path('create_task',views.TaskCreate,name='create'),
    path('update/<int:pk>',views.TaskUpdate,name='update'),
    path('delete/<int:pk>',views.TaskDelete,name='delete'),
    path('login/', views.TaskLogin, name='login'),
    path('logout/', views.TaskLogout, name = 'logout'),
    path('reg/', views.TaskReg, name='register')
]