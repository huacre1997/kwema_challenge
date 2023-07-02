from apps.bacteria.api.views import GetNumberOfBacteriaView
from django.urls import path

app_name = "bacteria"

urlpatterns = [
    path("count/", GetNumberOfBacteriaView.as_view(), name="bacteria_count"),
]
