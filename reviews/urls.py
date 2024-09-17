import requests
from django.urls import path, include
from rest_framework import routers
from .views import *


  # 'Authorization': 'Token 2001f864612daa65b58627cd09dd1ff5e2ca0a5fd6'
    # username = elenaterehova
    # password = elenaterehova


router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
