import json
from django.core import serializers
from django.forms.models import model_to_dict

from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles.models import Profile
from django.contrib.auth.models import User
from .serializers import ProfileSerializer, GetUsersEmailSerializer, GetProfilesAccountNumberSerializer, GetProfilesIppisNumberSerializer, GetProfilesNumberSerializer, GetUserSerializer

from rest_framework.permissions import IsAuthenticated

from django.http import HttpResponse




# Create your views here.
class ProfileCreate(generics.ListCreateAPIView):
  queryset = Profile.objects.all()
  serializer_class = ProfileSerializer


class ProfileDetail(generics.RetrieveAPIView):
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


class GetUser(APIView):
  permission_classes = [IsAuthenticated]
  serializer_class = GetUserSerializer

  def get(self, request, email, format=None):

    

    obj = User.objects.get(email=email)
    
    data = serializers.serialize('json', [obj,])

    struct = json.loads(data)
    data = json.dumps(struct[0])

    return HttpResponse(data)


class GetProfile(APIView):
  permission_classes = [IsAuthenticated]

  def get(self, request, user, format=None):

    obj = Profile.objects.get(user=user)

    data = serializers.serialize('json', [obj,])

    struct = json.loads(data)

    data = json.dumps(struct[0])

    return HttpResponse(data)

    



  

