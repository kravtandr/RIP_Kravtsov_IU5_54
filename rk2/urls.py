from django.urls import path
from rk import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('create_emp/', views.create_emp),
    path('edit/<int:id>/', views.edit),
    path('edit_department/<int:id>/', views.edit_department),
    path('delete/<int:id>/', views.delete),
    path('delete_department/<int:id>/', views.delete_department),
]
