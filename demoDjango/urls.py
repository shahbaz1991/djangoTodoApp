"""
URL configuration for demoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import redirect
from . import views
from django.views.generic import RedirectView
from django.conf.urls import handler404, handler500

urlpatterns = [
    path('', RedirectView.as_view(url='todoApp/', permanent=True)),
    path("todoApp/", views.home, name="BASE_URL"),
    path("todoApp/login/", include('login.urls'), name="login_url"),
    path("todoApp/register/", include('register.urls'), name="register_url"),
    path("todoApp/todoList/", include('todoList.urls'),  {'action':''}, name="todoList_url"),
    path("todoApp/todoList/delete/<int:task_id>/",include('todoList.urls'), {'action':'delete'}, name="todotask_delete"),
    path("todoApp/todoList/update/<int:task_id>/",include('todoList.urls') ,  {'action':'update'}, name="todotask_update"),
    path('todoApp/todoList/logout/', views.logout, name="logout_url"),
    path("admin/", admin.site.urls),
]

handler404 = views.errorRedirect
handler500 = views.errorRedirect