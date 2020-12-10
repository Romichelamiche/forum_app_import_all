from django.urls import path
from forumapp import views


app_name = "forumapp"
urlpatterns = [
    path('index', views.problem_index, name='index'),
    path('problem/detail/<int:pk>/', views.problem_detail, name="detail_problem"),
    path('problem/create/', views.problem_creation, name= "creation_problem"),
    path('problem/detail/<int:pk>/edit/', views.problem_edit, name="edit_problem"),
    path('problem/resolved/', views.problem_with_a_solution, name="liste des problemes avec solution"),
    path('problem/delete/<int:pk>/', views.delete_problem, name="delete"),
    path('login', views.login_user, name='login_function'),
    path('logout', views.logout_user, name='logout_function'),
    path('register', views.register_user, name='register_function'),
    path('edit_user', views.edit_user, name='edit_function'),
    path('problem/favorite/<int:pk>/', views.add_favorite, name='favorite'),
    path('problem/favorite/list/', views.list_favorite, name='favorite_list'),
    path('problem/favorite/<int:pk>/delete', views.delete_favorite, name='delete_favorite')

]