from django.shortcuts import render

def home_view(request):
    return render(request,"KimBoRam.html",{}) #{}=딕셔너리

def quote_view(request):
    return render(request,"quote.html",{})

def var_view(request):
    nums = [1,2,3,4,5]
    return render(request,"var.html",{"nums":nums})


# Create your views here.


