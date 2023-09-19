from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import LoginForm
from todoList.views import todoList
from login.models import ActivateUser
from register.models import RegisterModel
from django.views.decorators.cache import never_cache
from todoList.views import todoList

# Create your views here.
def loginUser(request):
    error = ''
    activeUser = ActivateUser.objects.all()
    if(activeUser):
        return HttpResponseRedirect(reverse(todoList))
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)

            if form.is_valid():
                user = form.cleaned_data['username']
                password = form.cleaned_data['password']
                foundUser = RegisterModel.objects.filter(username = user)
            
                if(len(foundUser) is not 0):
                    if(password == foundUser[0].password):
                        ActivateUser.objects.all().delete()
                        ActivateUser.objects.create(
                            token = foundUser[0].id,
                            user_details = foundUser[0]
                        )
                        return HttpResponseRedirect(reverse(todoList))
                    else:
                        error = 'Password is incorrect'
                        context = {
                            'form' : form,
                            'error' : error
                        }
                        return render(request,'login.html', context)
                else: 
                    error = 'User not Found'
                    context = {
                        'form' : form,
                        'error' : error
                    }
                    return render(request,'login.html', context)
        else :
            form = LoginForm(initial={
                'username' : '',
                'password' : ''
            })
        context = {
            'form' : form,
            'error' : error
        }
        return render(request,'login.html', context)