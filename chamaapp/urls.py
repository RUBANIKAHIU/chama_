from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'chamaapp'
router = DefaultRouter()
router.register(r'',views.chamaviewset, basename='chamaviewset')



urlpatterns = [
    path('', include(router.urls))
]