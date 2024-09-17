import requests
from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)


urlpatterns = [
    path('', include(router.urls)),

]
