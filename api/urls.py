from django.urls import path
from .views import LoanList, LoanDetails, UserLoginAPIView, UserRegistrationAPIView

urlpatterns = [
    path('loans/', LoanList.as_view(), name='loan-list'),  
    path('loans/<int:pk>/', LoanDetails.as_view(), name='loan-details'), 
    path('auth/register/', UserRegistrationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
]
