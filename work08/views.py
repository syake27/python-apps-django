from django.shortcuts import render, redirect, get_object_or_404
from .models import memo

# Create your views here.


def toppage(request):
    memos = memo.objects.all()
    return render(request, "work08/toppage.html", {"memos": memos})


# 新規作成
def new_memopage(request):
    memos = memo.objects.all()
    return render(request, "work08/memo.html", {"memos": memos})


# 編集
def memopage(request, id):
    memos = memo.objects.all()
    m = get_object_or_404(memo, id=id)
    return render(request, "work08/memo.html", {"memos": memos, "m": m})


def memo_create(request):
    if request.method == "POST":
        memo_title = request.POST.get("memo_title")
        memo_content = request.POST.get("memo_content")

        m = memo(memo_title=memo_title, memo_content=memo_content)
        m.save()

    return redirect("work08:toppage")


# ある程度できたけどメモ一覧から編集しようとした時に何も表示されないから
# 表示されるされるようにして編集できるようにしたい（多分idを取得してからdbでレコードを受け取って編集
# して保存する）


def memo_update(request, id):
    m = get_object_or_404(memo, id=id)
    if request.method == "POST":
        m.memo_title = request.POST.get("memo_title")
        m.memo_content = request.POST.get("memo_content")
        m.save()
    return redirect("work08:toppage")
