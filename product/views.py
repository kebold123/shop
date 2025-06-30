from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import User


def all(request):
    users = User.objects.all()
    return render(request, 'all.html', {'users': users})

def index(request):
    users = User.objects.filter(archived = False)
    return render(request, 'index.html', {'users': users})

def new(request):
    return render(request, 'new.html')

def create(request):
    if request.method == 'POST':
        user = User()
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.save()
    return HttpResponseRedirect("/")

def show(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.save()
        return HttpResponseRedirect("/")

    return render(request, 'show.html', {'user': user})

def delete(request, id):
    user = User.objects.get(id=id)
    user.archived = True
    user.save()
    return HttpResponseRedirect("/")

def recover(request, id):
    user = User.objects.get(id=id)
    user.archived = False
    user.save()
    return HttpResponseRedirect("/")

def about(request):
    return render(request, 'about.html')

def product(request, name):
    return render(request, 'product.html', {'name': name})

def postuser(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    # return render(request, 'about.html', {'name': name, 'age': age})
    return HttpResponse(f'<h2>Имя: {name}, Возраст: {age}</h2>')