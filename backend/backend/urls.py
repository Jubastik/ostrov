"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from backend.apps.camp.views import CampAPIList, CampAPIDetail, CampDetailAPIList, CampDetailAPIDetail, OtherPhtAPIList
from backend.apps.detection.views import DetectionAPIList
from backend.apps.weather.views import WeatherAPIList
from backend.apps.map import views as mapviews

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/camp/", CampAPIList.as_view()),
    path("api/camp/<int:pk>/", CampAPIDetail.as_view()),
    path("api/camp_detail/", CampDetailAPIList.as_view()),
    path("api/camp_detail/<int:pk>/", CampDetailAPIDetail.as_view()),
    path("api/camp_detail/other_pht", OtherPhtAPIList.as_view()),
    path("api/detection/", DetectionAPIList.as_view()),
    path("api/weather/", WeatherAPIList.as_view()),
    path("", mapviews.index, name="index")
]
