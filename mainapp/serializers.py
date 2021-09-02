from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
   """
   For checking and validating weather info (city, days)
   """
   city = serializers.CharField(max_length=100,required=True)
   days = serializers.IntegerField(default=1, min_value=1, max_value=3)