import datetime
import copy
import demoDjango
from django.shortcuts import render
from login.models import ActivateUser
from .forms import TodoForm
from .models import TodoListModal
from register.models import RegisterModel
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy

# Create your views here.
def todoList(request,action,task_id=False):
    activeUser = ActivateUser.objects.all()

    if(activeUser):
        userDetails = RegisterModel.objects.filter( id = activeUser[0].user_details.id)

        if request.method == 'POST':
            form = TodoForm(request.POST)
            if form.is_valid():
                if(action == 'update'):
                    TodoListModal.objects.filter(id=task_id).update(
                        title =  form.cleaned_data['title'],
                        description =  form.cleaned_data['description'],
                        dateTime =  form.cleaned_data['dateTime'],
                        completed = form.cleaned_data['completed'],
                        user_FK = userDetails[0]
                    )
                else:
                    todoDB = TodoListModal.objects.create(
                        title = form.cleaned_data['title'],
                        description = form.cleaned_data['description'],
                        dateTime = form.cleaned_data['dateTime'],
                        completed = form.cleaned_data['completed'],
                        user_FK = userDetails[0]
                    )
                    todoDB.save()
                return HttpResponseRedirect(reverse(todoList))
        else:
            form = TodoForm(initial={
                'title' : '',
                'description' : '',
                'completed' : False,
                'dateTime' : datetime.datetime.now().strftime("%Y-%m-%dT%H:%M"),
            })
            if(action == 'delete'):
                TodoListModal.objects.filter(id= task_id).delete()
                return HttpResponseRedirect(reverse(todoList))
            else:
                todoListFull = TodoListModal.objects.filter(user_FK = userDetails[0].id)
                sortedList = todoListFull.order_by("dateTime")
                currentDateList = sortedList.filter(dateTime__date=datetime.date.today())
                otherDateList = sortedList.exclude(dateTime__date=datetime.date.today())
                otherList = {}
                cd = ''
                print('ssadcvcxcvc',otherDateList,currentDateList)
                if(len(otherDateList) > 0):
                    for x in otherDateList:
                        if(cd != x.dateTime.date() ):
                            cd = x.dateTime.date()
                            otherList[cd] = [copy.copy(x)]
                        else :
                            otherList[cd].append(x)
                        print('pppp')
      
        context={
            'user': activeUser[0].user_details,
            'form' : form,
            'todoDetails': currentDateList,
            'otherList': otherList, 
            'minDate' : datetime.datetime.now(),
        }
        return render(request,'todoList/todolistmodal_form.html', context)
    else:
        return HttpResponseRedirect(reverse(demoDjango.views.home))