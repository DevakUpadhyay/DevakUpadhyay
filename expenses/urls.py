from django.urls import path
from . import views

urlpatterns = [
    path('create_report/', views.create_report, name='create_report'),
    path('report/<int:report_id>/', views.report_detail, name='report_detail'),
    path('reports/', views.report_list, name='report_list'),
    path('create_category/', views.create_category, name='create_category'),
    path('categories/', views.category_list, name='category_list'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
]
