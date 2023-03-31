from django.urls import path
from .views import contact

app_name = 'contact_app'

urlpatterns = [
    path('contact/', contact, name='contact'),
]