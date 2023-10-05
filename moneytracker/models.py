import datetime
from django.db import models
from django.urls import reverse

# Create your models here.
class Income(models.Model):
    name = models.CharField(max_length=100,unique=True,default="unknown")
    total_amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name}: {self.total_amount}"
    
    def get_absolute_url(self):
        return reverse("moneytracker:expense", kwargs={"pk": self.pk})
    
    class Meta():
        unique_together = ['name','total_amount']
    

class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("moneytracker:expense", kwargs={"pk": self.pk})    


class Expense(models.Model):
    total_amount = models.ForeignKey(Income,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today(),auto_created=True)
    expense_amount = models.PositiveIntegerField()
    text = models.CharField(max_length=128)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.expense_amount}"
    
    def get_absolute_url(self):
        return reverse("moneytracker:income", kwargs={"pk": self.pk})

