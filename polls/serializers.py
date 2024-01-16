from rest_framework import serializers 
from polls.models import Poll, Choice, Vote
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
       votes = VoteSerializer(many=True, required=False) 
       class Meta:
            model = Choice
            fields = '__all__'

class PollSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, read_only=True, required=False)
    class Meta:
        model = Poll
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}
    def created(self, validated_data):
         user = User(
              email=validated_data['email'],
              username=validated_data['username']
         )
         user.set_password(validated_data['passwords'])
         user.save()
         return user
     
