from django.urls import path
from cars import views

urlpatterns = [
    path('', views.home_page, name='home')
]
