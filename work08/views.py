from django.shortcuts import render, redirect, get_object_or_404
from .models import memo
from .forms import memoForm


# トップページ（一覧）
def toppage(request):
    memos = memo.objects.all().order_by("-created_at")
    return render(request, "work08/toppage.html", {"memos": memos})


# 新規メモ作成ページ
def new_memopage(request):
    form = memoForm()
    return render(request, "work08/memo.html", {"form": form})


# 編集ページ
def memopage(request, id):
    m = get_object_or_404(memo, id=id)
    form = memoForm(instance=m)  # ← 既存のデータをフォームに入れる
    return render(request, "work08/memo.html", {"form": form, "m": m})


# 新規メモ保存
def memo_create(request):
    if request.method == "POST":
        memo_title = request.POST.get("memo_title")
        memo_content = request.POST.get("memo_content")
        memo_image = request.FILES.get("memo_image")

        m = memo(
            memo_title=memo_title, memo_content=memo_content, memo_image=memo_image
        )
        m.save()

    return redirect("work08:toppage")


# 既存メモ更新
def memo_update(request, id):
    m = get_object_or_404(memo, id=id)
    if request.method == "POST":
        m.memo_title = request.POST.get("memo_title")
        m.memo_content = request.POST.get("memo_content")
        if "memo_image" in request.FILES:
            m.memo_image = request.FILES["memo_image"]
        m.save()
        return redirect("work08:toppage")
    return render(request, "work08/memo.html", {"m": m})


# メモ削除
def memo_delete(request, id):
    m = get_object_or_404(memo, id=id)
    if request.method == "POST":
        m.delete()
        return redirect("work08:toppage")
