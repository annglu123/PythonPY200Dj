from django.http import JsonResponse
from django.shortcuts import render
from .forms import TemplateForm


def index_view(request):
    if request.method == "GET":
        return render(request, 'landing/index.html')
    if request.method == "POST":
        received_data = request.POST  # Приняли данные в словарь
        form = TemplateForm(received_data)  # Передали данные в форму
        if form.is_valid():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]  # Получение IP
            else:
                ip = request.META.get('REMOTE_ADDR')  # Получение IP
            user_agent = request.META.get('HTTP_USER_AGENT')
            data = form.cleaned_data
            data["ip"] = ip
            data["user_agent"] = user_agent

            return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
        return render(request, 'landing/index.html', context={"form": form})