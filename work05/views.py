from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the work05 index.")


def profile(request):
    context = {
        "name": "犬塚　歩夢",
    }
    return render(request, "work05/index.html", context)
