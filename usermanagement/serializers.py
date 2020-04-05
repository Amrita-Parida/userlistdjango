from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField
from .models import *


class ActivityPeriodSerializer(serializers.ModelSerializer):
    start_time = SerializerMethodField()
    end_time = SerializerMethodField()
    def get_start_time(self,obj):
        time = obj.start_time.strftime('%Y-%m-%d %X')
        return time

    def get_end_time(self,obj):
        time = obj.end_time.strftime('%Y-%m-%d %X')
        return time
    class Meta:
        model = ActivityPeriod
        fields=('start_time','end_time')

class UserListSerializer(serializers.ModelSerializer):
    """User List Serializer get the list"""
    activity_periods = ActivityPeriodSerializer(source='user_activity',many=True)

    class Meta:
        model = MyUser
        fields = ('uuid','user_name','is_active','activity_periods')
