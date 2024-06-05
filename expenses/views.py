from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ExpenseReport, Expense, Category
from .forms import ExpenseReportForm, ExpenseForm, CategoryForm, UserRegistrationForm, UserLoginForm
from django.contrib.auth import login, authenticate

@login_required
def create_report(request):
    if request.method == 'POST':
        form = ExpenseReportForm(request.POST)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user  # Changed from 'employee' to 'user'
            report.save()
            return redirect('report_detail', report_id=report.id)
    else:
        form = ExpenseReportForm()
    return render(request, 'expenses/create_report.html', {'form': form})

@login_required
def report_detail(request, report_id):
    report = get_object_or_404(ExpenseReport, id=report_id)
    expenses = report.expenses.all()
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.report = report
            expense.save()
            return redirect('report_detail', report_id=report.id)
    else:
        form = ExpenseForm()
    return render(request, 'expenses/report_detail.html', {'report': report, 'expenses': expenses, 'form': form})

@login_required
def report_list(request):
    reports = ExpenseReport.objects.filter(user=request.user)  # Changed from 'employee' to 'user'
    print(reports)
    return render(request, 'expenses/report_list.html', {'reports': reports})

@login_required
def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.created_by = request.user
            category.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'expenses/create_category.html', {'form': form})

@login_required
def category_list(request):
    categories = Category.objects.filter(created_by=request.user)
    return render(request, 'expenses/category_list.html', {'categories': categories})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserRegistrationForm()
    return render(request, 'expenses/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                # Handle invalid login
                pass
    else:
        form = UserLoginForm()
    return render(request, 'expenses/login.html', {'form': form})
