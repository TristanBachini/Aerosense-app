from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import Token
import requests

token = ''
ip_address = ''

def log_in(request):
    
    #logging in
    if(request.method == 'POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            #login success
            url = "http://192.168.8.100/api/login"

            payload = "{\r\n    \"username\":\"admin\",\r\n    \"password\":\"admin\"\r\n}"
            headers = {
            'Content-Type': 'application/json;charset=UTF-8'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            data = response.json()
            
            #
            key = data.get('data', {}).get('token')

            Token.objects.update_or_create(user=request.user.id, token=key)


            return redirect('/home')
        
        else:
            print("Login Failed.")
#            messages.error(request, "Incorrect password or username")
        
        
    
    return render(request,"main/login.html")

@login_required(login_url='')
def home(request):
    return render(request,"main/home.html")

@login_required(login_url='')
def test_api(request):
    #Change this. Don't keep token as global variable.
    #First try storing it in database as part of the
    #user model. If successful, then lets do this.
    #If unsuccessful, let's try storing using session storage.
    
    global token

    url = "http://192.168.8.100/api/getIp"

    payload = ""
    headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json;charset=UTF-8',
    'Accept-Language': 'en'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

            



    return redirect('/home')



def set_ip(address):

    #match the API url used in web app
    global ip_address
    ip_address = address
    

