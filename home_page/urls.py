from django.urls import include, path
from .views import Contacts
urlpatterns = [
    path('contact-me/', Contacts.as_view() )
]