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

class CategoryCreateView(generic.CreateView):
    form_class = CategoryForm
    model = Category

class ExpenseCreateView(generic.CreateView):
    form_class = ExpenseForm 
    model = Expense   