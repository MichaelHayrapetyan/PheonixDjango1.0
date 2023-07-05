from django.urls import path
from manufacturers import views

app_name = 'company'
urlpatterns = [
    path('manufacturers/', views.company_view, name='Manufacturers'),
    path('details/<int:pk>/', views.company_detail, name='detail'),


]
