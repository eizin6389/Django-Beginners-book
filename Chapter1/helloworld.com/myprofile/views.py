from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def top(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html lang="ja">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Taro's Profile</title>
    </head>
    <body>
    <header>Taro's Profile</header>

    <nav>
        <a href="/">TOP</a>
        <a href="/resume">Resume</a>
    </nav>

    <h1>私についての概要</h1>
    <p>東京に住んでいる、40歳になったエンジニアです。</p>

    <h2>趣味</h2>
    <ul>
        <li>映画鑑賞</li>
    </ul>
    他の色々なコンテンツ...
    </body>
    </html>
    """)

def resume(request):
    return HttpResponse('職務経歴ページです!!!')
