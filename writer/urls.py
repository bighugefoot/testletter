from django.urls import path
from writer import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.index, name= 'index'),
    path('letterwrite/', views.writer, name= 'letterwrite'),
]