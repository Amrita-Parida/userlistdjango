from rest_framework import serializers
from datetime import datetime
from rest_framework.serializers import SerializerMethodField
from rest_framework.response import Response
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
    """merchant bank details for CRUD operations"""
    activity_periods = ActivityPeriodSerializer(source='user_activity',many=True)
    # r_bank_name = serializers.CharField(source='bank_name.name', read_only=True)
    # r_passbook = SerializerMethodField(read_only=True)

    class Meta:
        model = MyUser
        fields = ('uuid','user_name','is_active','activity_periods')