from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=15, default="DefaultUserName")
    status = serializers.IntegerField(default=0)

    class Meta:
        fields = ('id', 'name', 'status')
        model = models.User

    def create(self, validated_data):
        return models.User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.status = validated_data.get('status', instance.status)
        instance.save()
        return instance
