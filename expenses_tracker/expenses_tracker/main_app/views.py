from django.shortcuts import render, redirect

from expenses_tracker.main_app.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from expenses_tracker.main_app.models import Profile, Expense


def get_profile():
    profiles = Profile.objects.all()
    if profiles:
        return profiles[0]
    return None


def show_home_page(request):
    profile = get_profile()
    if profile:
        money_left = Profile.objects.first().budget - sum([exp.price for exp in Expense.objects.all()])
        context = {
            'expenses': Expense.objects.all(),
            'budget': Profile.objects.first().budget,
            'money_left': money_left,
        }
        return render(request, 'home-with-profile.html', context)
    else:
        if request.method == 'POST':
            form = CreateProfileForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('home page')
        else:
            form = CreateProfileForm()
        context = {
            'form': form
        }
        return render(request, 'home-no-profile.html', context)


def show_create_expense_page(request):
    form = Expense
    return render(request, 'expense-create.html')


def show_edit_expense_page(request, pk):
    return render(request, 'expense-edit.html')


def show_delete_expense_page(request, pk):
    return render(request, 'expense-delete.html')


def show_profile_page(request):
    profile = get_profile()
    expenses = Expense.objects.all()
    budget_left = Profile.objects.first().budget - sum([exp.price for exp in expenses])
    context = {
        'profile': profile,
        'expenses': expenses,
        'expenses_count': len(expenses),
        'budget_left': budget_left
    }
    return render(request, 'profile.html', context)


def show_profile_edit_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-edit.html', context)


def show_profile_delete_page(request):
    profile = get_profile()
    if request.method == 'POST':
        form = DeleteProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home page')
    else:
        form = DeleteProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'profile-delete.html', context)
