from django.shortcuts import render
import requests

token = ''
ip_address = ''

def home(request):
    
    if(request.method == 'POST'):

        url = "http://192.168.8.100/api/login"

        payload = "{\r\n    \"username\":\"admin\",\r\n    \"password\":\"admin\"\r\n}"
        headers = {
        'Content-Type': 'application/json;charset=UTF-8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

        data = response.json()
        
        #
        token = data.get('data', {}).get('token')



    return render(request,"main/login.html")

def set_token(request, key):
    
    #Set global token 
    global token 
    token = key
