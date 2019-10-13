from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'name', 'status', 'clearance')
        model = models.User
