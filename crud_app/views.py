from django.shortcuts import render
from rest_framework import generics
from .models import User
from crud_app.serializers import UserSerializer
# Create your views here.
class UserListCreat(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserRetriveUpdateDelete(generics.RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


