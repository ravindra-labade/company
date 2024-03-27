from django.urls import path
from .views import add_company, show_company, update_company, delete_company


urlpatterns = [
    path('add/', add_company, name='add_url'),
    path('show/', show_company, name='show_url'),
    path('update/<int:pk>/', update_company, name='update_url'),
    path('delete/<int:pk>/', delete_company, name='delete_url'),
]
