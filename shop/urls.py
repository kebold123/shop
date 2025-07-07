"""
URL configuration for shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from product import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.index, name='index'),
    path('new', views.new, name='new'),
    # path('index', views.index, name='index'),
    path('create', views.create, name='create'),
    path('show/<int:id>', views.show, name='show'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('about', views.about, name='about'),
    path('product/<str:name>', views.product, name='product'),
    path('postuser/', views.postuser, name='postuser'),
    path('all/', views.all, name='all'),
    path('recover/<int:id>', views.recover, name='recover'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
