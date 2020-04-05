from . import models
from rest_framework import serializers

class ActivityPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ActivityPeriod
        fields = ('start_time', 'end_time')

class MemberSerializer(serializers.ModelSerializer):
    activity_periods = ActivityPeriodSerializer(many=True, read_only=True)

    class Meta:
        model = models.Member
        fields = ('id', 'real_name', 'tz','activity_periods')


class UserSerializer(serializers.ModelSerializer):
    members = MemberSerializer(many=True, read_only=True)

    class Meta:
        model = models.User
        fields = ('ok','members')
