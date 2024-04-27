from rest_framework import generics, status
from .models import LoanApplication, CustomUser
from .serializers import  UserRegistrationSerializer, UserLoginSerializer,  LoanApplicationCreateSerializer, LoanApplicationRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken



class LoanList(generics.ListCreateAPIView):
    queryset = LoanApplication.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'POST':  # Use create serializer for POST requests
            return LoanApplicationCreateSerializer
        else:  # Use retrieve serializer for GET requests
            return LoanApplicationRetrieveSerializer




class LoanDetails(generics.RetrieveDestroyAPIView):
    queryset = LoanApplication.objects.all() 
    serializer_class = LoanApplicationRetrieveSerializer 
    
    


class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistrationSerializer
    


class UserLoginAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            login_data = serializer.validated_data
            return Response(login_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)