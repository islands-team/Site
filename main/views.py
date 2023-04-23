from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

# Create your views here
new_user = User.objects.all()

def reg(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(index)
        else:
            error = 'Форма была неверной'



    form = UserForm()

    data = {
        'form':form,
        'error':error
    }

    return render(request, 'main/reg.html', data)

def index(request):
    return render(request, 'main/index.html')

def cabinet(request):
    return render(request, 'main/cabinet.html')

