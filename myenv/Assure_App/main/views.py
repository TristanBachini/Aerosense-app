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
        set_token(token)
    
    return render(request,"main/login.html")


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

            



    return render(request,"main/login.html")

def set_token(key):
    
    #Set global token 
    global token 
    token = key


def set_ip(address):

    #match the API url used in web app
    global ip_address
    ip_address = address
    

