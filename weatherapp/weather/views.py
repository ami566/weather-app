from django.shortcuts import render
import requests
import os
key = os.environ.get('weather_api_key')
#print(key)

def index(request):
    if request.method == 'POST': 
        city = request.POST['city']
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + str(key)
        #city = 'Sofia'
        #print(url)
        try: 
            weather_data = requests.get(url.format(city)).json()
            weather = {
                'city' : city,
                "country_code": weather_data['sys']['country'], 
                'temperature' : str(weather_data['main']['temp']) + "° C",
                'description' : weather_data['weather'][0]['description'],
                'icon' : weather_data['weather'][0]['icon']
            }
        except:
            weather = { 'city': "The given place could not be found" }

    else:
        weather = []
    context = {'weather' : weather}
    return render(request, 'weather/index.html', context) 
