#Rendering html pages
from django.shortcuts import render,redirect

from django.db import IntegrityError # occurs when there is an attempt to insert or update data that violates constraints such as unique constraints, foreign key constraints, or other database-specific constraints.

#rest_framework codes
# Importing Serializer
# Serializer converts complex data types to json
#A viewset is a way to organize the logic for handling different HTTP methods (e.g., GET, POST, PUT) on a resource
# AllowAny is a permissive permission class that allows any user, whether authenticated or not, to access the associated view or endpoint.

from rest_framework import serializers
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action


from django.contrib.auth.models import User

#importing my models
from .models import Profile,Members



class DummySerializer(serializers.Serializer):
    # look later with research
    pass

class chamaviewset(viewsets.ModelViewSet): 
    permission_classes = (AllowAny,)
    serializer_class = DummySerializer

# Render signup.html
    @action(detail=False, methods= ['get','post'])
    def signup(self,request):
        if request.method == 'POST':
            first_name = request.POST.get('fname')
            last_name = request.POST.get('lname')
            phone_number = request.POST.get('phone')
            email= request.POST.get('email')
            gender= request.POST.get('gender')
            date_of_birth= request.POST.get('dob')
            password= request.POST.get('password')

            
             # Check if phone number already exists
            if User.objects.filter(username=phone_number).exists():
                phone_numberError = "The  phone number already exits"
                return render(request, 'signup.html', {'phone_numberError': phone_numberError, 'emailError': ''})

            # Check if email already exists
            if User.objects.filter(email=email).exists():
                emailError = "The email already exits"
                return render(request, 'signup.html', {'emailError': emailError, 'phone_numberError': ''})
            
            try:
                    # Create user in chamaapp
                    user = User.objects.create_user(
                        username=phone_number,
                        email=email,
                        password=password
                    )

                    
                    # Create user profile in chamaapp
                    profile = Profile.objects.create (
                        user=user,
                        first_name = first_name,
                        last_name =last_name,
                        phone_number= phone_number,
                        email=email,
                        gender=gender,
                        date_of_birth=date_of_birth
                    )




                    # Redirect to success page or perform other actions
                    profile.save() 
                    return redirect('http://127.0.0.1:8000/user_login/')
            
            except IntegrityError as e:
                 print(f"Error {e}")
            
        return render(request, 'signup.html')
      
#Render login.html
    @action(detail=False, methods= ['get','post'])
    def user_login(self,request):

        if request.method == 'POST':
             
             phone_number = request.POST.get('phone')
             password = request.POST.get('password')
             user = User.objects.filter(username=phone_number).first()


             if user:
                  print(user)
                  if user.check_password(password):
                       return redirect ('http://127.0.0.1:8000/home/')

                  else:
                       print('unsuccesful login')
                       
             else:
                print('User not found')
             
                  
        return render(request, 'login.html')
    
#Render homepage
    @action(detail=False, methods= ['get','post'])
    def home(self,request):
        return render(request, 'homepage.html')
    
#render totalfunds
    @action(detail=False, methods= ['get','post'])
    def totalfunds(self,request):
        return render(request, 'totalfunds.html')

#render list of members
    @action(detail=False, methods= ['get','post'])
    def members_list(self,request):
        members = Members.objects.select_related('profile').all()
        return render(request, 'listofmembers.html',  {'members': members})

        


    




 