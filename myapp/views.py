from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    city = request.GET.get('city','kochi')
    url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=e24aa0cedb48b90c1b91f07e65f80067'
    data = requests.get(url).json()

    payload = {
    'city':data['name'],
    'weather':data['weather'][0]['main'],
    'description':data['weather'][0]['description'],
    'icon':data['weather'][0]['icon'],
    'temperature':int(data['main']['temp'] - 273),
    'max_temperature':int(data['main']['temp_max'] - 273),
    'min_temperature':int(data['main']['temp_min'] -273),
    'pressure':data['main']['pressure'],
    'humidity':data['main']['humidity']




}

    context = {'data':payload}


    return render(request,'weather/index.html',context)
