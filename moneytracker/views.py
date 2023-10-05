from typing import Any
from django.db import models
from django.shortcuts import render
from django.views import generic
from moneytracker.forms import IncomeForm, CategoryForm, ExpenseForm
from moneytracker.models import Income, Category, Expense

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = 'moneytracker/base.html'

class IncomeCreateView(generic.CreateView):
    form_class = IncomeForm
    model = Income

class IncomeListView(generic.ListView):
    model = Income    

class CategoryCreateView(generic.CreateView):
    form_class = CategoryForm
    model = Category

class ExpenseCreateView(generic.CreateView):
    form_class = ExpenseForm 
    model = Expense

    def get_queryset(self,pk):
        return Income.objects.get(id=pk)

# def show_income(request,pk):
#     income = Income.objects.get(id=pk)
#     return income



