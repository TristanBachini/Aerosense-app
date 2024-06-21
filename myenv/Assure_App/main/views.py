from django.shortcuts import render
import requests

def home(request):
    
    if(request.method == 'POST'):
        print("allo")
    return render(request,"main/login.html")
