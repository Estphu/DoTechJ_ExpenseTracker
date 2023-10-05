from django.urls import path
from . import views

app_name = 'moneytracker'

urlpatterns = [
    path('income/',views.IncomeCreateView.as_view(),name='income'),
    path('<int:pk>/',views.ExpenseCreateView.as_view(),name='expense'),
    path('category/',views.CategoryCreateView.as_view(),name='category'),
    path('',views.IncomeListView.as_view(),name='incomelist')
]
