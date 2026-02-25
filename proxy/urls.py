from django.urls import path
from . import views

urlpatterns = [
    path('', views.AsyncProxyView.as_view(), name='proxy'),
]


