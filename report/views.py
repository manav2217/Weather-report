from django.shortcuts import render
import requests
import time
import datetime

# Create your views here.

def index(request):
    if request.method == "POST":
        try:
            search_city = request.POST['ct']
            url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=9817ef2447af066b4e3aa0a8901d2a85"
        
            city = search_city 
            date = datetime.datetime.today().date
            r = requests.get(url.format(city)).json()
            print(r)
            city_weather = {
                'city' : city,
                'date' : date,
                'temperature' : r['main']['temp'],
                'wind' : r['wind']['speed'],
                'icon' : r['weather'][0]['icon'],
                'desc' : r['weather'][0]['description'],
            }   
            data = {'data' : city_weather}
            
            return render(request , "index.html" , data)
        except:
            return render(request , "index.html")
    else:
        return render(request, "index.html")
