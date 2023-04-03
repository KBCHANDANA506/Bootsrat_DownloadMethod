from django.shortcuts import render

# Create your views here.

def MDB4_parent(request):
    return render(request,'MDB4_parent.html')

def child(request):
    return render(request,'child.html')