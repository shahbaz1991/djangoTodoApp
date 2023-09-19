from django.shortcuts import render, get_object_or_404
from register.forms import RegistrationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import RegisterModel
from login.views import loginUser
from todoList.views import todoList
from login.models import ActivateUser

# Create your views here.
def registerUser(request):
    error = ''
    activeUser = ActivateUser.objects.all()
    if(activeUser):
        return HttpResponseRedirect(reverse(todoList))
    else:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)

            if form.is_valid():
                userExist = RegisterModel.objects.filter(email = form.cleaned_data['email'])

                print('exist', userExist)
                if(len(userExist) is 0):
                    registerDB = RegisterModel.objects.create(
                        name = form.cleaned_data['name'],
                        mobile = form.cleaned_data['mobile'],
                        email = form.cleaned_data['email'],
                        username = form.cleaned_data['username'],
                        password = form.cleaned_data['password']
                    )
                    registerDB.save()
                    return HttpResponseRedirect(reverse(loginUser))
                else:
                    error = 'Account already exist'
                    context = { 'form' : form, 'error': error }
                    return render(request, 'register.html', context)
        else:
            form = RegistrationForm(initial={
                'name' : '',
                'mobile' : '',
                'email' : '',
                'username' : '',
                'password' : '',
            })

        context = { 'form' : form, 'error': error}
        return render(request, 'register.html', context)