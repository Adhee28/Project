from django.urls import path
from sendmails import views

urlpatterns=[
    path( ''  ,views.mail)
]