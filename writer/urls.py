from django.urls import path
from writer import views

urlpatterns = [
    path('', views.index, name= 'index'),
    path('letterwrite/', views.writer, name= 'letterwrite'),
]