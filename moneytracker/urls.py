from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='base'),
    path('category/',views.CategoryCreateView.as_view(),name='category'),
]
