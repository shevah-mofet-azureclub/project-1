from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home),
    path('riddle/', views.riddle),
    path('riddle/answer/', views.answer),
    path('multiply', views.multiply),
]
