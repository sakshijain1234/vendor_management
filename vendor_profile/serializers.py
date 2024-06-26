from rest_framework import serializers
from .models import vendor_model

class vendors_serializer(serializers.ModelSerializer):
    class Meta():
        model=vendor_model
        fields="__all__"

class vendor_serializer(serializers.ModelSerializer):
    class Meta():
        model=vendor_model
        exclude = ['vendor_code']

class performance_serializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_model
        fields = [
            'name',
            'vendor_code',
            'on_time_delivery_rate',
            'quality_rating_avg',
            'average_response_time',
            'fulfillment_rate'
        ]

    
    
    

    
    
