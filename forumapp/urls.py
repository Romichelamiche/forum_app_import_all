from django.urls import path
from forumapp import views

app_name = "forumapp"
urlpatterns = [
    path('', views.problem_index, name='index'),
    path('problem/detail/<int:pk>/', views.problem_detail, name="detail_problem"),
    path('problem/create/', views.problem_creation, name= "creation_problem"),
    path('problem/detail/<int:pk>/edit/', views.problem_edit, name="edit_problem"),
    path('problem/resolved/', views.problem_with_a_solution, name="liste des problemes avec solution"),
    path('problem/search/', views.search, name="search"),
    path('problem/delete/<int:pk>/', views.delete_problem, name="delete"),



]