from django.db import models

# Create your models here.
class Login(models.Model):
    username=models.CharField(max_length=90)
    password=models.CharField(max_length=90)
    type=models.CharField(max_length=90)

class restaurant(models.Model):
    lid=models.ForeignKey(Login,on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    phonenumber=models.BigIntegerField()
    email=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    image=models.ImageField()
    pin=models.IntegerField()
    district=models.CharField(max_length=50)
    license=models.BigIntegerField()
    lattitude=models.CharField(max_length=1000)
    longitude = models.CharField(max_length=1000)


class resorts(models.Model):
    lid = models.ForeignKey(Login, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    phonenumber = models.BigIntegerField()
    email = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    image = models.ImageField()
    pin = models.IntegerField()
    district = models.CharField(max_length=50)
    license = models.BigIntegerField()
    lattitude = models.CharField(max_length=1000)
    longitude = models.CharField(max_length=1000)

class touristplace(models.Model):
    place=models.CharField(max_length=50)
    image=models.ImageField()
    latitude=models.CharField(max_length=50)
    longitude=models.CharField(max_length=50)
    description=models.CharField(max_length=50)

class userregistration(models.Model):
    lid=models.ForeignKey(Login, on_delete=models.CASCADE)
    fullname=models.CharField(max_length=50)
    address=models.CharField(max_length=60)
    gender=models.CharField(max_length=50)
    phonenumber = models.BigIntegerField()
    email = models.CharField(max_length=50)

class feedback(models.Model):
    uid=models.ForeignKey(userregistration,on_delete=models.CASCADE)
    feedbacks=models.CharField(max_length=1000)
    date=models.DateField()

class restaurantreviewrating(models.Model):
    uid=models.ForeignKey(userregistration,on_delete=models.CASCADE)
    restaurantid = models.ForeignKey(restaurant, on_delete=models.CASCADE)
    review=models.CharField(max_length=60)
    rating=models.FloatField()
    date = models.DateField()

class resortreviewrating(models.Model):
    uid=models.ForeignKey(userregistration,on_delete=models.CASCADE)
    resortid = models.ForeignKey(resorts, on_delete=models.CASCADE)
    review=models.CharField(max_length=60)
    rating=models.FloatField()
    date = models.DateField()

class touristplacereviewrating(models.Model):
    uid = models.ForeignKey(userregistration, on_delete=models.CASCADE)
    tpid = models.ForeignKey(touristplace, on_delete=models.CASCADE)
    review = models.CharField(max_length=60)
    rating = models.FloatField()
    date = models.DateField()


class fooditem(models.Model):
    category=models.CharField(max_length=90)
    restaurantid=models.ForeignKey(restaurant,on_delete=models.CASCADE)
    foodname=models.CharField(max_length=60)
    image=models.ImageField()
    description=models.CharField(max_length=60)
    price=models.FloatField()

class restaurantfacility(models.Model):
    restaurantid=models.ForeignKey(restaurant,on_delete=models.CASCADE)
    facility=models.CharField(max_length=60)
    description=models.CharField(max_length=70)
    image=models.ImageField()

class resortfacility(models.Model):
    resortid=models.ForeignKey(resorts,on_delete=models.CASCADE)
    facility=models.CharField(max_length=60)
    description=models.CharField(max_length=70)
    image=models.ImageField()

class resortroom(models.Model):
    resortid=models.ForeignKey(resorts,on_delete=models.CASCADE)
    roomno=models.IntegerField()
    type=models.CharField(max_length=20)
    image=models.FileField()
    amount=models.FloatField()

class complaints(models.Model):
    userid=models.ForeignKey(userregistration,on_delete=models.CASCADE)
    complaint=models.CharField(max_length=1000)
    date=models.DateField()
    reply=models.CharField(max_length=1000)

