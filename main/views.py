from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Items
from .forms import CreateNewList
from django.contrib.auth.models import User
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    
    #{"save":["save"]}
    if response.method == "POST":
        print(response.POST)
        
        if response.POST.get("save"):
            print(response.POST.get("save"))
            pass
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            print(response.POST.get("newItem"))
            print(txt)
            pass

    
    return render(response, "main/list.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            #response.user.todolist.add(t)
        
        return HttpResponseRedirect("/%i" %t.id)
    else:
        
        form = CreateNewList()
    return render(response, "main/create.html", {"form":form})



def view(response):
    return render(response, "main/view.html",{})