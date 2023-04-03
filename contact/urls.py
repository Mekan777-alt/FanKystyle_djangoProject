from django.urls import path
from .views import contact, checkout

app_name = 'contact_app'

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('create/', checkout, name='create'),
]