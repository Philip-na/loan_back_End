from rest_framework import serializers
from .models import LoanApplication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'account_number','id']
      


class LoanApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ['name', 'email', 'phone', 'amount', 'duration_months', 'reason', 'user','status','approved_date']
        
        
class LoanApplicationRetrieveSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # Include user details in retrieval

    class Meta:
        model = LoanApplication
        fields = ['id', 'name', 'email', 'phone', 'amount', 'duration_months', 'reason', 'user','approved_date', 'status']


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'email', 'date_of_birth', 'account_number']
        extra_kwargs = {
            'password': {'write_only': True}
        }
        
        

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
      
        # self.send_registration_email(user)
        return user   
    # def send_registration_email(self, user):
    #     subject = 'Welcome to Grop 2!'
    #     message = f'Hi {user.username},\n\nThank you for registering with us. Enjoy our services!'
    #     from_email = ''
    #     recipient_list = [user.email]
    #     send_mail(subject, message, from_email, recipient_list)
    

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = CustomUser.objects.filter(username=username).first()

            if user and user.check_password(password):
               
                return {
                    'user': user.username,  
                    'id': user.id,
                    'email': user.email,
                    'account_number': user.account_number,
                  
                }
            raise serializers.ValidationError('Invalid credentials')
        raise serializers.ValidationError('Must include "username" and "password"')