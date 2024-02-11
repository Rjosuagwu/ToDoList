from django.shortcuts import get_object_or_404, render, redirect
from .models import Task
from .forms import TaskForm, TaskFormUpdate
from django.contrib import messages #display messages in a user friendly manner

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

# Create your views here.

@login_required
def TaskList(request):

    task = Task.objects.all().filter(user=request.user)


    search_input = request.GET.get('search-area') or ''

    if search_input:
        task = Task.objects.all().filter(user=request.user).filter(title__startswith=search_input)

    context = {
        "task":task,
        "search_input":search_input
    }

    return render(request,'base/tasks.html',context)


@login_required
def TaskDetails(request,pk): # pk will be the Task object i am specifying
    task = get_object_or_404(Task, pk=pk)
    context = {
        "task":task
    }
    return render(request,'base/details.html',context)

@login_required
def TaskCreate(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False) # this is used to create a task instance but not save it yet
            task.user = request.user #associate the user with the currently logged in user
            task.save()
            return redirect('tasks')
    else:
        form = TaskForm()
    context = {"form":form}
    return render(request,'base/create.html',context)

@login_required
def TaskUpdate(request,pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskFormUpdate(request.POST,instance=task) #we need to specify the instance to have the initial fields
        if form.is_valid():
            form.save()
            return redirect('tasks')
    else:
        form = TaskFormUpdate(instance=task)

    context = {
        "form":form
               }
    return render(request,'base/update.html',context)

@login_required
def TaskDelete(request,pk): # pk will be the Task object i am specifying
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
        messages.success(request, 'You have successfully deleted the task.')
        return redirect('tasks')
    context = {
        "task":task
    }
    return render(request,'base/delete.html',context)


def TaskReg(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login')
        else:
            context ={
                'error':'Invalid credentials',
                'form' : form
            }
            return render(request,'base/reg.html',context)
    else:
        form = UserCreationForm()

    return render(request, 'base/index.html', {'form':form})


def TaskLogin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'You have successfully logged in.')
            return redirect('tasks')
        else:
            context ={
                'error':'Invalid credentials',
                'form' : form
            }
            return render(request,'base/login.html',context)
    else:
        form = AuthenticationForm()

    return render(request,'base/login.html', {'form':form})

def TaskLogout(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return render (request,'base/tasks.html')
    
        
