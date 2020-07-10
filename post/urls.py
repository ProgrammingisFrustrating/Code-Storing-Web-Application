from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_index, name='post'),
    path('add_project/', views.add_post, name='newpost'),
    path('project/<str:pk>/', views.single_post, name='singlePost'),
    path('update/<str:pk>/', views.update, name='updateTask'),
    path('delete/<str:pk>/', views.delete, name='deleteTask'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]