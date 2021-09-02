from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from .serializers import WeatherSerializer
import requests
import json
import math
import os
import yaml
from rest_framework.decorators import action
from django.conf import settings


def api_docs(request):
    """
    Base API Docs endpoint function for the Swagger
    """
    file = open(os.path.join(settings.BASE_DIR, 'api.yaml'), encoding='utf8')
    spec = yaml.safe_load(file.read())
    return render(request, template_name="swagger_base.html", context={'data': json.dumps(spec)})


class WeatherViewSet(ViewSet):
    """
    General ViewSet for Weather API
    """
    serializer_class = WeatherSerializer

    @action(methods=['get'], detail=False, url_path=r'(?P<city>[\w-]+)/', url_name='get_weather')
    def get(self, request, *args, **kwargs):
        data = {'city': kwargs.get(
            'city', None), 'days': request.GET.get('days', 1)}
        serializer = WeatherSerializer(data=data)
        if serializer.is_valid():
            weather = []
            data = {}
            response = json.loads(requests.get(
                f'{settings.BASE_WEATHER_API_URL}forecast.json?key={settings.WEATHER_API_KEY}&q={serializer.data["city"]}&days={serializer.data["days"]}&aqi=no&alerts=no').content)
            
            if "error" in response:
                return Response(response['error']['message'],status=400)

            data['location'] = response['location']['name']
            for d in response['forecast']['forecastday']:
                day = {
                    "date": d["date"],
                    "maximum": d["day"]["maxtemp_c"],
                    "minimum": d["day"]["mintemp_c"],
                    "average": d["day"]["avgtemp_c"]
                }
                hours = []
                for hour in d['hour']:
                    hours.append(hour['temp_c'])
                hours.sort()
                if len(hours) % 2 == 0:
                    middle = int(len(hours)/2)
                    day['median'] = round(
                        (hours[middle] + hours[middle+1])/2, 2)
                else:
                    day['median'] = round(hours[math.ceil(len(hours)/2)], 2)
                weather.append(day)
            data['weather'] = weather
            return Response(data)
        return Response(serializer.errors,status=400)
