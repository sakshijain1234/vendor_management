from rest_framework import serializers
from .models import PurchaseOrder

class po_serializer(serializers.ModelSerializer):
    class Meta():
        model=PurchaseOrder
        fields="__all__"

# class po_acknowledge(serializers.ModelSerializer):
#     def set_acknowledge():
#         data=PurchaseOrder.acknowledgment_date

# class vendor_serializer(serializers.ModelSerializer):
#     class Meta():
#         model=PurchaseOrder
#         exclude = ['po_number']