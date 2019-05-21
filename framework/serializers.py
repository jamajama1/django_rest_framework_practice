from django.contrib.auth.models import User, Group
from rest_framework import serializers
from framework.models import  Interns


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class InternsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Interns
        fields= ('name', 'field_of_study', 'year')