from django.shortcuts import render
from .serializers import RegisterSerializer

from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# Register
class RegisterAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


# Logout
@api_view(['POST'])
def logout(request):
    request.user.auth_token.delete()
    return Response({'message': 'User Logout: Token Deleted!'})