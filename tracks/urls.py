from django.urls import path
from .views import tracks

app_name = 'track_app'

urlpatterns = [
    path('tracks/', tracks, name='track'),
]