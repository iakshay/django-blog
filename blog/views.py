from django.http import HttpResponse


def home(request):
    return HttpResponse('<h1>Hey Joe</h1>')


def greeting(request, name):
    return HttpResponse("<h1>Hey %s</h1>" % name)
