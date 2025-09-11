from django.shortcuts import render
from .forms import reiwaform
from .forms import bmiForm
from .forms import warikanForm
from .forms import chokinFrom
from .forms import calculatorForm

# Create your views here.


def reiwa(request):
    form = reiwaform(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            year = form.cleaned_data["year"]
            reiwa_year = year + 2018
            return render(
                request,
                "work06/index.html",
                {"form": form, "reiwa_year": reiwa_year, "year": year},
            )
    return render(request, "work06/index.html", {"form": form})


def top(request):
    return render(request, "work06/toppage.html")


def bmi(request):
    form = bmiForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            height = form.cleaned_data["height"]
            weight = form.cleaned_data["weight"]
            bmi = weight / (height * height)
            bmi = round(bmi, 2)
            if bmi < 18.5:
                result = "低体重"
            elif 18.5 <= bmi < 25:
                result = "普通体重"
            elif 25 <= bmi < 30:
                result = "肥満(1度)"
            elif 30 <= bmi < 35:
                result = "肥満(2度)"
            elif 35 <= bmi < 40:
                result = "肥満(3度)"
            else:
                result = "肥満(4度)"
            return render(
                request,
                "work06/bmi.html",
                {
                    "form": form,
                    "bmi": bmi,
                    "result": result,
                    "height": height,
                    "weight": weight,
                },
            )
    return render(request, "work06/bmi.html", {"form": form})


def warikan(request):
    form = warikanForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            total_amount = form.cleaned_data["total_amount"]
            people = form.cleaned_data["people"]
            person = total_amount // people
            remainder = total_amount % people
            return render(
                request,
                "work06/warikan.html",
                {
                    "form": form,
                    "total_amount": total_amount,
                    "people": people,
                    "person": person,
                    "remainder": remainder,
                },
            )
    return render(request, "work06/warikan.html", {"form": form})


def chokin(request):
    form = chokinFrom(request.POST or None)
    month = [
        "1か月",
        "2か月",
        "3か月",
        "4か月",
        "5か月",
        "6か月",
        "7か月",
        "8か月",
        "9か月",
        "10か月",
        "11か月",
        "12か月",
    ]
    if request.method == "POST":
        if form.is_valid():
            chokin_amount = form.cleaned_data["chokin_amount"]
        for i in range(1, 13):
            total = chokin_amount * i
            if i == 1:
                total_list = [total]
            else:
                total_list.append(total)

        combined = zip(month, total_list)

        return render(
            request,
            "work06/chokin.html",
            {
                "form": form,
                "chokin_amount": chokin_amount,
                "combined": combined,
            },
        )
    return render(request, "work06/chokin.html", {"form": form})


def calculator(request):
    form = calculatorForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            number1 = form.cleaned_data["number1"]
            number2 = form.cleaned_data["number2"]
            add = number1 + number2
            subtract = number1 - number2
            multiply = number1 * number2
            if number2 != 0:
                divide = round(number1 / number2, 2)
            else:
                divide = "エラー"
            return render(
                request,
                "work06/calculator.html",
                {
                    "form": form,
                    "number1": number1,
                    "number2": number2,
                    "add": add,
                    "subtract": subtract,
                    "multiply": multiply,
                    "divide": divide,
                },
            )
    return render(request, "work06/calculator.html", {"form": form})