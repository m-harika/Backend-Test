from django.shortcuts import render
from activity.serializers import UserSerializer,MemberSerializer,ActivityPeriodSerializer
from rest_framework import viewsets
from .models import User,Member,ActivityPeriod

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

class ActivityPeriodViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivityPeriodSerializer
