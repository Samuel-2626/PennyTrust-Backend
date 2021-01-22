from rest_framework import serializers
from profiles.models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):

  class Meta:
    fields = ('user', 'title', 'first_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'city', 'state', 'place_of_work', 'loan_amount', 'tenor', 'address', 'ippis_number', 'salary_bank_name', 'account_number', 'referral_code')
    model = Profile 


class GetUsersEmailSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('email',)


class GetProfilesNumberSerializer(serializers.ModelSerializer):

  class Meta:
    model = Profile
    fields = ('phone_number',)


class GetProfilesAccountNumberSerializer(serializers.ModelSerializer):

  class Meta:
    model = Profile
    fields = ('account_number',)


class GetProfilesIppisNumberSerializer(serializers.ModelSerializer):

  class Meta:
    model = Profile
    fields = ('ippis_number',)