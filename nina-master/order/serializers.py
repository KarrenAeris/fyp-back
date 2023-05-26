from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
        model = Order
        fields = '__all__'
        read_only_fields = ['user', 'status', 'price', 'name']


class OrderSerializerDetail(serializers.ModelSerializer):
    # image = Base64ImageField()
    class Meta:
        model = Order
        fields = ['price', ]
