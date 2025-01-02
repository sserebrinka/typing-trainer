from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect
from django.contrib import messages
from .models import UserProfile, TestResult
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from datetime import datetime


@login_required
def profile_view(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = UserProfile.objects.create(user=request.user)
        messages.info(request, "Ваш профиль был создан автоматически.")

    test_results = TestResult.objects.filter(user_profile=user_profile).order_by('-test_date')

    total_tests = test_results.count()
    total_time = sum(result.time_taken for result in test_results)
    record_speed = test_results.order_by('-speed').first().speed if test_results.exists() else 0

    if request.method == 'POST':
        username = request.POST.get('username', request.user.username)
        first_name = request.POST.get('first_name', request.user.first_name)
        last_name = request.POST.get('last_name', request.user.last_name)
        email = request.POST.get('email', request.user.email)

        if User.objects.exclude(pk=request.user.pk).filter(username=username).exists():
            messages.error(request, "Это имя пользователя уже занято.")
        elif User.objects.exclude(pk=request.user.pk).filter(email=email).exists():
            messages.error(request, "Этот email уже используется.")
        else:
            if 'avatar' in request.FILES:
                user_profile.avatar = request.FILES['avatar']
            user_profile.save()

            request.user.username = username
            request.user.first_name = first_name
            request.user.last_name = last_name
            request.user.email = email
            request.user.save()

            messages.success(request, "Профиль успешно обновлен.")
            return redirect('users:profile')

    return render(request, 'users/profile.html', {
        'user_profile': user_profile,
        'test_results': test_results,
        'total_tests': total_tests,
        'total_time': total_time,
        'record_speed': record_speed,
    })


@login_required
def delete_test_results(request):
    if request.method == 'POST':
        selected_results = request.POST.getlist('selected_results')
        
        if selected_results:
            TestResult.objects.filter(id__in=selected_results).delete()
            messages.success(request, "Выбранные результаты успешно удалены.")
        else:
            messages.error(request, "Не выбраны результаты для удаления.")
    
    return redirect('users:profile')


@login_required
def update_test_results(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        speed = data.get('speed')
        accuracy = data.get('accuracy')
        time_taken = data.get('time_taken')

        user_profile, created = UserProfile.objects.get_or_create(user=request.user)

        TestResult.objects.create(
            user_profile=user_profile,
            speed=speed,
            accuracy=accuracy,
            time_taken=time_taken,
            test_date=datetime.now()
        )

        return JsonResponse({'status': 'success'})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в систему!')
            return redirect('users:profile')
        else:
            messages.error(request, 'Неверные имя пользователя или пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'users/login.html', {'form': form})


def registration_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Регистрация прошла успешно!', extra_tags='registration')
            return redirect('users:login')
        else:
            messages.error(request, 'Произошла ошибка при регистрации', extra_tags='registration')
    else:
        form = UserCreationForm()

    return render(request, 'users/registration.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    messages.info(request, 'Вы вышли из системы.')
    return redirect('users:login')
