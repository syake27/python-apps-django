from django.shortcuts import render
import random

# Create your views here.


def top(request):
    return render(request, "work07/toppage.html")


def omikuji(request):
    omikuji = None
    if "draw" in request.GET:
        omikuji_list = [
            "大吉",
            "中吉",
            "小吉",
            "吉",
            "末吉",
            "凶",
            "大凶",
        ]
        omikuji = random.choice(omikuji_list)
    return render(request, "work07/omikuji.html", {"omikuji": omikuji})


def janken(request):
    result = None
    if "guu" in request.GET:
        player = "グー"
        computer = random.choice(["グー", "チョキ", "パー"])
    elif "choki" in request.GET:
        player = "チョキ"
        computer = random.choice(["グー", "チョキ", "パー"])
    elif "paa" in request.GET:
        player = "パー"
        computer = random.choice(["グー", "チョキ", "パー"])
    else:
        return render(request, "work07/janken.html")
    if player == computer:
        result = "あいこ"
    elif (
        (player == "グー" and computer == "チョキ")
        or (player == "チョキ" and computer == "パー")
        or (player == "パー" and computer == "グー")
    ):
        result = "勝ち"
    else:
        result = "負け"
    return render(
        request,
        "work07/janken.html",
        {"player": player, "computer": computer, "result": result},
    )


def hi_low(request):
    result = None

    number_set = request.GET.get("number_set")
    if number_set is not None:
        number_set = int(number_set)
    else:
        number_set = random.randint(1, 10)  # 初回はランダムで作る

    # 勝負の数字
    number = random.randint(1, 10)

    if "HI" in request.GET:
        if number > number_set:
            result = "当たり"
        else:
            result = "はずれ"
    elif "LOW" in request.GET:
        if number < number_set:
            result = "当たり"
        else:
            result = "はずれ"

    return render(
        request,
        "work07/hi_low.html",
        {
            "number": number,
            "number_set": number_set,
            "result": result,
        },
    )
