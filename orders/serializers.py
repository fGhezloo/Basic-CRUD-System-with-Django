from rest_framework import serializers
from django.core.validators import RegexValidator
from .models import Order

class OrderSerializer(serializers.Serializer):
    phone_regex = RegexValidator(regex=r'^(\+98|0)?9\d{9}$', message="Phone number must be entered in the format: '09999999999' or '+989999999999'.")
    email_regex = RegexValidator(regex=r'^\w[\w\.-]*@\w[\w\.-]+\.\w+$', message="Enter a valid Email address")
    dateTime=serializers.DateTimeField()
    purchase=serializers.CharField(max_length=150)
    purchaseID=serializers.IntegerField()
    userID=serializers.IntegerField()
    name=serializers.CharField(max_length=150)
    phoneNumber=serializers.CharField(validators=[phone_regex], max_length=20)
    email=serializers.EmailField(validators=[email_regex])
    address=serializers.CharField()


    def create(self, validated_data):
        return Order.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.dateTime = validated_data.get('dateTime', instance.dateTime)
        instance.purchase = validated_data.get('purchase', instance.purchase)
        instance.purchaseID = validated_data.get('purchaseID', instance.purchaseID)
        instance.userID = validated_data.get('userID', instance.userID)
        instance.name = validated_data.get('name', instance.name)
        instance.phoneNumber = validated_data.get('phoneNumber', instance.phoneNumber)
        instance.email = validated_data.get('email', instance.email)
        instance.address = validated_data.get('address', instance.address)

        instance.save()
        return instance