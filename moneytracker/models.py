import datetime
from django.db import models

# Create your models here.
class Income(models.Model):
    total_amount = models.PositiveIntegerField()

class Category(models.Model):
    title = models.CharField(max_length=30)    


class Expense(models.Model):
    total_amount = models.ForeignKey(Income,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today(),auto_created=True)
    expense_amount = models.PositiveIntegerField()
    text = models.CharField(max_length=128)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

