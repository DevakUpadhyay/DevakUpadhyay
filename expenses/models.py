from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class ExpenseReport(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
        ('Paid', 'Paid'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field for monetary amounts
    date = models.DateField(blank=True, null=True, help_text='today date.')  # Date field for storing dates
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)  # DateTime field for creation timestamp

    def __str__(self):
        return self.title

class Expense(models.Model):
    report = models.ForeignKey(ExpenseReport, related_name='expenses', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Decimal field for monetary amounts
    date = models.DateField()  # Date field for storing dates
    description = models.TextField()

    def __str__(self):
        return f"{self.category} - {self.amount}"

class Comment(models.Model):
    report = models.ForeignKey(ExpenseReport, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # DateTime field for creation timestamp

    def __str__(self):
        return f"Comment by {self.user} on {self.report}"
