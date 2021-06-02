from django.shortcuts import render
from testapp.models import student
from django.db.models import Q
from django.http import HttpResponse
from django.db.models import Avg,Sum,Max,Count
from . import forms
def thankyou(request):
    return render(request,'testapp/thankyou.html')
def home(request):
    return render(request,'testapp/home.html')
def registration(request):
    if request.method =="POST":
        form = forms.studentregistration(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return render(request,'testapp/register.html',{'form':form})
        


    if request.method == "GET":
        form = forms.studentregistration()
        return render(request,'testapp/register.html',{'form':form})
    

def list1(request):
    student1 = student.objects.all()
    
    
    return render(request,'testapp/thankyou.html',{'student':student1})


def middleware(request):
    print(10/0)
    print('This statement is executed from middleware view function')
    return HttpResponse('<h1>Custom Middleware Demo</h1>')
    

# Create your views here.
