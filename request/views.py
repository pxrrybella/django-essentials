from django.shortcuts import render
import requests

# Create your views here.
r = requests.get('https://api.waifu.pics/sfw/waifu')
data = r.json()

def request(request):
    return render(request, 'request/request.html', {'data': data})
