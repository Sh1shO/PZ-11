from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world!</h1>")

def second_page(request):
    return render(request, 'second_page.html')

def odin(request):
    return render(request, '1.html')
def second_awdawdpage(request):
    return render(request, '2.html')
def second_page(request):
    return render(request, '3.html')
def second_page(request):
    return render(request, '4.html')
def second_page(request):
    return render(request, '5.html')