from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import List, History

# Create your views here.
def index(request):
    # data = List.objects.all()
    query = request.GET.get('search','')
    if query:
        data = List.objects.filter(task__icontains=query)
    else:
        data = List.objects.all()
    
    context = {
        'data' : data
    }

    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        task = request.POST.get('task') 
        a = List.objects.create(task = task)
        # print(task)
        return redirect('home')

    return render(request,'add.html')

def update(request, pk):
    data1 = List.objects.get(id = pk)
    if request.method == 'POST':
        action = request.POST.get('action')  # Check which action (update or delete)

        if action == 'update':
            # Handle Update Action
            task = request.POST.get('task')
            if not task:  # If task is empty
                return HttpResponse("Task cannot be empty!", status=400)
            data1.task = task
            data1.save()
            return redirect('home')  # Redirect to the home page

    context = {
        'data1': data1
        }
    
    return render(request, 'update.html', context)

def delete(request,pk1):
    data1 = List.objects.get(id = pk1)  # Get the task object to delete
    b = History.objects.create(dtask = data1.task)

    data1.delete()  # Delete the task

    return redirect('home')

def hist(request):
    data2 = History.objects.all()
    context = {
        'data2' : data2
    }
    return render(request,'history.html',context)

def pdelete(request,pk2):
    print("one")
    data2 = History.objects.get(id=pk2)
    if request.method == 'POST':
        data2.delete()
    
    return redirect('home')
