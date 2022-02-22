from django.shortcuts import render, redirect

from djangoProject1.web.forms import CreateProfile, CreateExpense, EditProfile, DeleteProfile, EditExpense, \
    DeleteExpense
from djangoProject1.web.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_create_profile(request):
    if request.method == 'POST':
        form = CreateProfile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreateProfile()
    no_profile = True
    context = {
        'form': form,
        'no_profile': no_profile,
    }
    return render(request, 'home-no-profile.html', context)


def show_home_page(request):
    profile = get_profile()
    if not profile:
        return redirect('create profile')
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    items = Expense.objects.count()
    context = {
        'profile': profile,
        'expenses': expenses,
        'budget_left': budget_left,
        'items': items,
    }
    return render(request, 'home-with-profile.html', context)


def show_create_expense(request):
    if request.method == 'POST':
        expenses_form = CreateExpense(request.POST, request.FILES)
        if expenses_form.is_valid():
            expenses_form.save()
            return redirect('home')
    else:
        expenses_form = CreateExpense()
    context = {
        'expenses_form': expenses_form,
    }
    return render(request, 'expense-create.html', context)


def show_edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    form = EditExpense(request.POST, request.FILES, instance=expense)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
        return redirect('home')
    form = EditExpense(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-edit.html', context)


def show_delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteExpense(request.POST, request.FILES, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = DeleteExpense(instance=expense)
    context = {
        'form': form,
        'expense': expense,
    }
    return render(request, 'expense-delete.html', context)


def show_profile(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = profile.budget - sum(e.price for e in expenses)
    items = Expense.objects.count()
    context = {
        'profile': profile,
        'budget_left': budget_left,
        'items': items
    }
    return render(request, 'profile.html', context)


def show_edit_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        form_edit_profile = EditProfile(request.POST, request.FILES, instance=profile)
        if form_edit_profile.is_valid():
            form_edit_profile.save()
            return redirect('profile')
    else:
        form_edit_profile = EditProfile(instance=profile)

    context = {
        'form_edit_profile': form_edit_profile,
    }
    return render(request, 'profile-edit.html', context)


def show_delete_profile(request):
    profile = get_profile()
    if request.method == 'POST':
        delete_form = DeleteProfile(request.POST, request.FILES, instance=profile)
        if delete_form.is_valid():
            delete_form.save()
            return redirect('home')
    else:
        delete_form = DeleteProfile(instance=profile)

    context = {
        'delete_form': delete_form,
    }

    return render(request, 'profile-delete.html')
