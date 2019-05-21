from django.shortcuts import render

from django.contrib.auth.models import User, Group
from framework.models import Interns
from rest_framework import viewsets
from framework.serializers import UserSerializer, GroupSerializer, InternsSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class InternsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Interns.objects.all()
    serializer_class = InternsSerializer