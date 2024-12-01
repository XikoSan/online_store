
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import UserRegisterForm
from django.http import JsonResponse


def register(request):
    if request.user.is_authenticated:
        return redirect('account')

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Логиним пользователя после регистрации
            messages.success(request, 'Аккаунт успешно создан!')
            return JsonResponse({'success': True})
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки ниже.')
            return JsonResponse({'success': False, 'errors': form.errors})

    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


def account(request):
    return render(request, 'users/account.html')


@login_required
def account_view(request):
    return render(request, 'users/account.html')
