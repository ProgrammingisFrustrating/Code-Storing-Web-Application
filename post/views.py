from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.db.models import Q
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def post_index(request):
    model = CodeModel.objects.all()
    query = request.GET.get('q')
    if query:
        model = model.filter(
            Q(name__icontains=query)|
            Q(status__icontains=query)|
            Q(lang__name__icontains=query)
            ).distinct()
    content = {'models': model}
    return render(request, 'post/index.html', content)
    
@login_required(login_url='login')
def single_post(request, pk):
    models = CodeModel.objects.get(id=pk)
    content = {'models':models}
    return render(request, 'post/detail_code.html', content)

@login_required(login_url='login')
def add_post(request):
    form = CodeForm()
    content = {'form':form}
    if request.method == "POST":
        form = CodeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'post/add_project.html', content)

@login_required(login_url='login')
def update(request, pk):
    code = CodeModel.objects.get(id=pk)
    form = CodeForm(instance=code)

    if request.method == 'POST':
        form = CodeForm(request.POST,request.FILES, instance=code)
        if form.is_valid():
            form.save()
        return redirect('/')
    content = {'form':form}
    return render(request, 'post/update.html', content)

@login_required(login_url='login')
def delete(request, pk):
    item = CodeModel.objects.get(id=pk)
    content = {'item':item}
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, "post/delete.html", content)

def login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = auth.authenticate(username=name, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('post')
        else:
            messages.info(request, 'invalid')
            return redirect('login')
    return render(request, 'post/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')