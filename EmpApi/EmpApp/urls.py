from django.urls import path
from . import views
  
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.Emp_list),
    path('update/<int:pk>/', views.Emp_detail, name='update-items'),

      
]