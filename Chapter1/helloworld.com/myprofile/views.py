from django.http import HttpResponse
from django.template import loader

def top(request):
    html = loader.render_to_string('myprofile/top.html')
    return HttpResponse(html)

def resume(request):
    return HttpResponse('職務経歴ページです!!!')
