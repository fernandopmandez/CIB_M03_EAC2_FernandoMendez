from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my Django site!")

urlpatterns = [
    path("", home, name="home"),  # This makes '/' return a welcome page
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
