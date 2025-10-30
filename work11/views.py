from django.shortcuts import render
from django.http import HttpResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv  # ← 安全のため追加


def simple_qa(request):
    # .env ファイルを読み込み（なければ無視）
    load_dotenv()

    # Google Gemini APIキーを取得
    api_key = os.getenv("GOOGLE_API_KEY")  # ← 正しい環境変数名に変更！
    if not api_key:
        return HttpResponse("❌ GOOGLE_API_KEY が設定されていません。")

    # API設定
    genai.configure(api_key=api_key)

    # 質問を取得
    question = request.GET.get("question", "おすすめのレシピは？")

    # モデル選択
    model = genai.GenerativeModel("gemini-2.0-flash")

    # プロンプト生成
    prompt = f"質問: {question}\n回答:"

    print(f"送信するプロンプト: {prompt}\n")

    # テキスト生成を実行
    response = model.generate_content(prompt)

    return HttpResponse(f"<pre>{response.text}</pre>")
