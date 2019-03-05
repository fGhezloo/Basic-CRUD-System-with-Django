from django.db import models
from django.core.validators import RegexValidator


class Order(models.Model):
    dateTime=models.DateTimeField()
    purchase=models.CharField(max_length=150)
    purchaseID=models.IntegerField(primary_key=True)
    userID=models.IntegerField()
    name=models.CharField(max_length=150)
    phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$', message="Phone number must be entered in the format: '09999999999' or '+989999999999'.")
    phoneNumber=models.CharField(validators=[phone_regex], max_length=20)
    email=models.EmailField()
    address=models.TextField()

    def __str__(self):
    	return str(self.purchaseID)