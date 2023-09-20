from django import forms
from moneytracker.models import Expense, Category, Income

class IncomeForm(forms.ModelForm):
    
    class Meta():
        fields = ['total_amount']
        model = Income

class CategoryForm(forms.ModelForm):

    class Meta():
        fields = ['title']
        model = Category

class ExpenseForm(forms.ModelForm):
        
    class Meta():    
        fields = ['expense_amount','text'] 
        model = Expense       

