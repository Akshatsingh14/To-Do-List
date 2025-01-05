from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from .models import List, History
from .forms import Register

# Create your views here.

# Login Function
def log_in(request):
    if request.method == 'POST':
        un = request.POST['un']
        password = request.POST['password']

        # Authenticate the user
        user = authenticate(request, username=un, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Provide feedback for invalid credentials
            return HttpResponse("Invalid credentials, please try again!")

    return render(request, 'enter.html')


# Logout Function
def log_out(request):
    logout(request)
    return redirect('log_in')


# Registration Function
def register(request):
    if request.method == 'POST':
        # Instantiate the form with POST data
        form = Register(request.POST)
        
        if form.is_valid():
            # Extract username and password from the form
            un = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            try:
                # Additional manual password validation
                validate_password(password)

                # Save the user (form's save method handles hashing the password)
                user = form.save()

                # Authenticate and log in the user
                login(request, user)
                return redirect('home')  # Redirect to home page or desired location

            except Exception as e:
                # Handle errors during additional validation
                return HttpResponse(f"Error: {str(e)}", status=400)
        else:
            # Provide feedback if the form is invalid
            return render(request, 'register.html', {'register': form})

    else:
        # Render an empty form for GET requests
        form = Register()
        return render(request, 'register.html', {'register': form})


# Display Tasks
@login_required(login_url='log_in')
def index(request):
    query = request.GET.get('search', '')

    # Filter tasks based on search query
    if query:
        data = List.objects.filter(task__icontains=query, user=request.user).order_by('-id')
    else:
        data = List.objects.filter(user=request.user).order_by('-id')

    context = {'data': data}
    return render(request, 'index.html', context)


# Create a New Task
@login_required(login_url='log_in')
def create(request):
    if request.method == 'POST':
        task = request.POST.get('task')

        # Prevent empty task creation
        if not task.strip():
            return HttpResponse("Task cannot be empty!", status=400)

        # Create the task
        List.objects.create(task=task, user=request.user)
        return redirect('home')

    return render(request, 'add.html')


# Update a Task
@login_required(login_url='log_in')
def update(request, pk):
    data1 = get_object_or_404(List, id=pk, user=request.user)

    if request.method == 'POST':
        action = request.POST.get('action')

        if action == 'update':
            task = request.POST.get('task')

            # Prevent empty task update
            if not task.strip():
                return HttpResponse("Task cannot be empty!", status=400)

            data1.task = task
            data1.save()
            return redirect('home')

    context = {'data1': data1}
    return render(request, 'update.html', context)


# Delete a Task
@login_required(login_url='log_in')
def delete(request, pk1):
    data1 = get_object_or_404(List, id=pk1, user=request.user)

    if request.method == 'POST':
        History.objects.create(dtask=data1.task, user=request.user)  # Include user
        data1.delete()
        return redirect('home')

    return HttpResponse("Method Not Allowed", status=405)


# View History of Deleted Tasks
@login_required(login_url='log_in')
def hist(request):
    data2 = History.objects.filter(user=request.user).order_by('-id')
    context = {'data2': data2}
    return render(request, 'history.html', context)


# Delete a Task from History
@login_required(login_url='log_in')
def pdelete(request, pk2):
    data2 = get_object_or_404(History, id=pk2, user=request.user)

    if request.method == 'POST':
        data2.delete()
        return redirect('hist')

    return HttpResponse("Method Not Allowed", status=405)