from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from weather.forms import CustomUserCreationForm
from weather.utilities import checkweather
from django.contrib.auth.views import LoginView, LogoutView
from weather.models import City
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
from weather.serializers import CitySerializer

# 1. authentication views
class SignUp(CreateView):
    """A SignUp instance of CreateView for Signing Up the user.

    Args:
        CreateView (class): A view with login to create an instance of a table in database.
    """
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "weather/signup.html"


class Login(LoginView):
    """A class to handle login action for user.

    Args:
        LoginView (class): A class with inbuilt functionality for Login.
    """
    success_url = reverse_lazy("home")
    template_name = "weather/login.html"


class Logout(LogoutView):
    """A class with Logout action.

    Args:
        LogoutView
    """
    pass
# end authentication view


# 2. homepage view
def homepage(request):

    # Home page view with implementation of representing 
    # weather data and saving it in database simultaneously.

    # cities = ["delhi", "mumbai", "kolkata", "bengaluru", "hyderabad"]
    cities = City.objects.all()
    for city in cities:
        city_weather = checkweather(city.city_name)
        obj,created = City.objects.update_or_create(pk=city_weather["city_name"],
            defaults={
            "city_country":city_weather["city_country"],
            "temp":city_weather["temp"],
            "pressure":city_weather["pressure"],
            "humidity":city_weather["humidity"],
            "weather":city_weather["weather"],
            "icon":city_weather["icon"],
        })
        obj.save()

    data = City.objects.all()
    return render(request, "weather/home.html", {"weathers": data})


# API views
@api_view(["GET"])
def endpoints(request):
    
    # a api view for represting the endpoints of api

    data = {
        "/api/cities/",
        "/api/cities/<str:city_name>/",
    }
    return Response(data)


class ListCityAPI(generics.ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DetailCityAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    lookup_field = "city_name"
    permission_classes = [IsAuthenticated]
