from django.urls import path, include
from rest_framework import routers
from mainapp import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'locations', views.WeatherViewSet, basename='Weather')

urlpatterns = [
    path('', views.api_docs, name="api_docs"),
    path('api/', include(router.urls))
]
