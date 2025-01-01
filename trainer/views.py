from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TypingTestText
import random
from django.views.decorators.csrf import csrf_exempt


def learn(request):
    return render(request, 'trainer/learn/learn.html')


def typing_test(request):
    if 'custom_text' in request.session:
        text_to_type = request.session.pop('custom_text')
    else:
        texts = TypingTestText.objects.all()
        text_to_type = random.choice(texts).text if texts else "Тексты для тренировки не добавлены."

    return render(request, 'trainer/test/test.html', {
        'text_to_type': text_to_type,
    })


def custom(request):
    if request.method == "POST":
        custom_text = request.POST.get("custom_text").strip()
        if custom_text:
            if len(custom_text) > 1:
                request.session['custom_text'] = custom_text
                return redirect('typing_test')
            else:
                messages.error(request, "Текст должен состоять более чем из одной буквы.", extra_tags='custom')
        else:
            messages.error(request, "Пожалуйста, введите текст.", extra_tags='custom')

    return render(request, 'trainer/custom/custom.html')


