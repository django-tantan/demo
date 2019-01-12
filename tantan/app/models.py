from django.db import models

# Create your models here.
class User(models.Model):
    phonenum = models.CharField(max_length=20,primary_key=True)
    nickname = models.CharField(max_length=20)
    sex = models.BooleanField(default=0)
    birth_year = models.IntegerField(max_length=20)
    birth_month = models.IntegerField(max_length=20)
    birth_day = models.IntegerField(max_length=20)
    avatar = models.TextField()
    location = models.CharField(max_length=64)
    token = models.CharField(max_length=128)
    @classmethod
    def create(cls,phonenum,nickname,sex,birth_year,birth_month,birth_day,avatar,location,token):
        return cls(phonenum=phonenum,nickname=nickname,sex=sex,birth_year=birth_year,birth_month=birth_month,birth_day=birth_day,avatar=avatar,location=location,token=token)
    class Meta:
        db_table="user"

class Profile(models.Model):

    location = models.ForeignKey("User",max_length=40)
    min_distance = models.CharField(max_length=40)
    max_distance = models.CharField(max_length=40)
    min_dating_age = models.IntegerField(max_length=20)
    max_dating_age = models.IntegerField(max_length=20)
    dating_sex = models.BooleanField()
    vibration = models.BooleanField(default=None)
    only_matche = models.BooleanField(default=None)
    auto_play = models.BooleanField(default=1)
    @classmethod
    def create(cls,location,min_distance,max_distance,min_dating_age,max_dating_age,dating_sex,vibration,only_matche,auto_play):
        return cls(location=location,min_distance=min_distance,max_distance=max_distance,min_dating_age=min_dating_age,max_dating_age=max_dating_age,dating_sex=dating_sex,vibration=vibration,only_matche=only_matche,auto_play=auto_play)
    class Meta:
        db_table = "profile"



