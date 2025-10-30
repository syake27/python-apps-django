from django.shortcuts import render


def app_list(request):
    return render(request, "python_apps_django/app_list.html")
