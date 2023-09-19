from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from login.models import ActivateUser
from todoList.views import todoList

def home(request):
    activeUser = ActivateUser.objects.all()
    if(activeUser):
        return HttpResponseRedirect(reverse(todoList))
    else:
        return render(request,'initialPage.html')

def logout(request):
    activeUser = ActivateUser.objects.all()
    ActivateUser.objects.all().delete()
    return HttpResponseRedirect(reverse(home))

def errorRedirect(request, exception='NONE'):
    activeUser = ActivateUser.objects.all()
    if(activeUser):
        return HttpResponseRedirect(reverse(todoList))
    else:
        return HttpResponseRedirect(reverse(home))
