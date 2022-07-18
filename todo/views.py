from django.shortcuts import redirect, render
from .models import Todo

# Create your views here.


def todo(request):
    if request.method == "POST":
        # if method is POST that we will store todo value into data base
        todo = request.POST.get('todo')
        print(todo)
        Todo.objects.create(todo=todo)
        return redirect('/')

    if request.GET.get('id'):
        # toggle completed according by getting id of that specify todo
        todo = Todo.objects.get(id=request.GET.get('id'))
        todo.is_completed = not todo.is_completed
        todo.save()

        # get all the todo data form the data base and send context while rendering html element
    context = {'todos': Todo.objects.all()}

    # rendering html template into home page
    return render(request, 'todo.html', context)
