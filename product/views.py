from django.shortcuts import render
from django.http import HttpResponse



def home(request):
    return render(request, 'home.html')
    # return HttpResponse("Домашняя страница")

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def product(request, name):
    return render(request, 'product.html', {'name': name})

def postuser(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    # return render(request, 'about.html', {'name': name, 'age': age})
    return HttpResponse(f'<h2>Имя: {name}, Возраст: {age}</h2>')