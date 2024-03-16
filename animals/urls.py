"""
URL configuration for animals project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from pets.views import TurtleView, TurtleViewID, DogView, CatView, BirdView, DogViewID, CatViewID, BirdViewID

urlpatterns = [
    path('admin/', admin.site.urls),
    path('turtle/', TurtleView.as_view(), name='turtle-list'),
    path('turtle/<int:id>/', TurtleViewID.as_view(), name='turtle-detail'),
    path('dog/', DogView.as_view(), name='dog-list'),
    path('dog/<int:id>/', DogViewID.as_view(), name='dog-detail'),
    path('cat/', CatView.as_view(), name='cat-list'),
    path('cat/<int:id>/', CatViewID.as_view(), name='cat-detail'),
    path('bird/', BirdView.as_view(), name='bird-list'),
    path('bird/<int:id>/', BirdViewID.as_view(), name='bird-detail'),
]
