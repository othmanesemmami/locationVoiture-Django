from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_car_view, name='create_car'),
    path('update/<int:car_id>/', views.update_car_view, name='update_car'),
    path('delete/<int:car_id>/', views.delete_car_view, name='delete_car'),
    path('delete_all/', views.delete_all_cars_view, name='delete_all_cars'),
    path('list/', views.car_list_view, name='car_list'),
    path('main_menu/', views.main_menu_view, name='main_menu'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.logout_view, name='logout'),
    path('main/', views.main_menu_view, name='home'),  # Default path to the main menu
]
