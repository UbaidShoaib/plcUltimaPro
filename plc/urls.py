from django.urls import path
from plc import views


urlpatterns = [
    path('', views.index, name='index')
]