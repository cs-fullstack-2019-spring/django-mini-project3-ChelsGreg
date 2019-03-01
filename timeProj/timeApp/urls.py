from django.urls import path
from . import views

# ROUTING PATHS TO FUNCTIONS
urlpatterns = [
    path('', views.index, name='index'),
    path('/teacherInfo/<int:id>/', views.teacherInfo, name='teacherInfo'),
    path('/newTeacher/', views.newTeacher, name='newTeacher'),
    path('/edit/<int:id>/', views.edit, name='edit'),
    path('/delete/<int:id>/', views.delete, name='delete'),
    path('schoolHours/<int:id>/', views.schoolHours, name='schoolHours'),

]