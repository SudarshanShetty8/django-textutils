from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")


def index1(request):
    tt1 = request.GET.get('a', 'default')
    check1 = request.GET.get('c', "off")
    pact = "!,.[]{}()-+=_*&^%$#@!:;?/><"
    answer1 = ""
    check = request.GET.get('b', 'off')
    if check == 'on':
        for char in tt1:
            if char not in pact:
                answer1 = answer1 + char

    elif check1 == 'on':
        pact1 = "\n"
        for char in tt1:
            if char not in pact1:
                answer1=answer1+char

    params = {'tt': tt1, 'answer':answer1}
    return render(request, 'index1.html', params)
