#Rendering html pages
from django.shortcuts import render

#rest_framework codes
# Importing Serializer
# Serializer converts complex data types to json
#A viewset is a way to organize the logic for handling different HTTP methods (e.g., GET, POST, PUT) on a resource
# AllowAny is a permissive permission class that allows any user, whether authenticated or not, to access the associated view or endpoint.

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action

#importing my models
from .models import Profile 
from .models import Login


class DummySerializer(serializers.Serializer):
    # look later with research
    pass

class chamaviewset(viewsets.ModelViewSet): 
    permission_classes = (AllowAny,)
    serializer_class = DummySerializer

# Render signup.html
    @action(detail=False, methods= ['get','post'])
    def signup(self,request):
        return render(request, 'signup.html')
    
#Render login.html
    @action(detail=False, methods= ['get','post'])
    def login(self,request):
        return render(request, 'login.html')

    




 