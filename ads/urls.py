from django.contrib import admin
from django.urls import path, include

from ads import views
from ads.views import Category, Ad, CategoryDetail, AdDetail

urlpatterns = [
    path('', views.get),
    path('cat/', Category.as_view()),
    path('ad/', Ad.as_view()),
    path('cat/<int:pk>/', CategoryDetail.as_view()),
    path('ad/<int:pk>/', AdDetail.as_view()),
]