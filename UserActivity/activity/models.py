from django.db import models
import pytz
#from django.contrib.auth import get_user_model

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

# Create your models here.
class User(models.Model):
    ok = models.BooleanField(default=True)

    def __str__(self):
        return str(self.ok)

class Member(models.Model):
    user = models.ForeignKey(User,related_name='members',on_delete=models.CASCADE)
    id = models.CharField(max_length=256,primary_key=True)
    real_name = models.CharField(max_length=256)
    tz = models.CharField(max_length=32,choices=TIMEZONES,default='UTC')

    def __str__(self):
        return self.real_name

class ActivityPeriod(models.Model):
    member = models.ForeignKey(Member,related_name='activity_periods',on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
