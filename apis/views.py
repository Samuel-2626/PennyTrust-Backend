from django.shortcuts import render
from rest_framework import generics
from profiles.models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, GetUsersEmailSerializer, GetProfilesAccountNumberSerializer, GetProfilesIppisNumberSerializer, GetProfilesNumberSerializer, GetUserSerializer

from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ProfileCreate(generics.ListCreateAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer


class GetUsersEmail(generics.ListAPIView):
  queryset = User.objects.all()
  serializer_class = GetUsersEmailSerializer


class GetProfilesIppisNumber(generics.ListAPIView):
  queryset = Profile.objects.all()
  serializer_class = GetProfilesIppisNumberSerializer


class GetProfilesAccountNumber(generics.ListAPIView):
  queryset = Profile.objects.all()
  serializer_class = GetProfilesAccountNumberSerializer


class GetProfilesNumber(generics.ListAPIView):
  queryset = Profile.objects.all()
  serializer_class = GetProfilesNumberSerializer


class GetUser(generics.ListAPIView):
  permission_classes = [IsAuthenticated,]
  queryset = User.objects.all()
  serializer_class = GetUserSerializer