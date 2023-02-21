from django.urls import path
from .views import TaskView, TaskCreate, TaskUpdate,TaskDelete, TaskDetail
from .views import CustomLoginView,signup,signin,signout


# class based view

urlpatterns= [
    path('LoginView/',CustomLoginView.as_view(),name='login'),
    path('Tasklist/',TaskView.as_view(), name='items'),
    path('create/',TaskCreate.as_view(), name='create_items'),
    path('Task-Update/<int:pk>/', TaskUpdate.as_view(), name='update_items'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),
    path('details/<int:pk>',TaskDetail.as_view(),name='detail_items'),
    path('signup',signup,name='signup'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),

]
