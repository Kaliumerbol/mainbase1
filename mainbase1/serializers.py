from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Mainbase1
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', ]

class Mainbase1Serializer(serializers.ModelSerializer):
    estimated_finish_time = serializers.DateTimeField()
    owner = UserSerializer(read_only=True)
    class Meta:
        model = Mainbase1
        fields = ['id', 'owner', 'reg_id', 'register_at', 'pr_name', 'pr_zacaz', 'pr_proectir', 'finished_at', 'estimated_finish_time', 'is_finished', ]
        read_only_fields = ['is_finished', ]