from django.urls import path, include
from weather.views import (
    Login,
    Logout,
    SignUp,
    DetailCityAPI,
    ListCityAPI,
    homepage,
    endpoints,
)
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("registration/", SignUp.as_view(), name="signup"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("", homepage, name="home"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("api/", view=endpoints, name="api"),
    path("api/cities/", view=ListCityAPI.as_view(), name="listcity"),
    path(
        "api/cities/<str:city_name>/", view=DetailCityAPI.as_view(), name="detailedcity"
    ),
]
