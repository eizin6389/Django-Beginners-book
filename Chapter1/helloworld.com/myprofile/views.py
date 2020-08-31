from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def top(request):
    return HttpResponse('トップページです!!!')

def resume(request):
    return HttpResponse('職務経歴ページです!!!')
