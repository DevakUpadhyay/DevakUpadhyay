from django.contrib import admin
from .models import ExpenseReport, Expense, Category

class ExpenseReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'amount', 'date', 'user', 'status', 'created_at')
    search_fields = ('title', 'user__username', 'status')
    list_filter = ('status', 'created_at')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('report', 'category', 'amount', 'date', 'description')
    search_fields = ('report__title', 'category__name')
    list_filter = ('date', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_by')
    search_fields = ('name', 'created_by__username')
    list_filter = ('created_by',)

admin.site.register(ExpenseReport, ExpenseReportAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Category, CategoryAdmin)
