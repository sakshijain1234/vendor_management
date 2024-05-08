from rest_framework import serializers
from .models import vendor_model,PerformanceRecord
from purchase_order.models import PurchaseOrder
from django.db.models import F,Avg
from datetime import timezone,datetime

class vendors_serializer(serializers.ModelSerializer):
    class Meta():
        model=vendor_model
        fields="__all__"

class vendor_serializer(serializers.ModelSerializer):
    class Meta():
        model=vendor_model
        exclude = ['vendor_code']

class performance_serializer(serializers.ModelSerializer):
    class Meta():
        model=PerformanceRecord
        fields="__all__"

    def date():
        today=datetime.now(timezone.utc)
        return today

    def Delivery_rate(instance):
        # records=PurchaseOrder.objects.filter(vendor=instance.vendor)
        on_time_count = PurchaseOrder.objects.filter(
        vendor=instance.vendor,
        status='completed',
        delivery_date__lte=F("issue_date")
        ).count()
        total_completed_count = PurchaseOrder.objects.filter(
        vendor=instance.vendor, 
        status='completed'
        ).count()
        rate = 0
        if total_completed_count > 0:
            rate = on_time_count/total_completed_count
        return rate
    
    def av_quality_rating(instance):
        average = PurchaseOrder.objects.filter(
        vendor=instance.vendor,
        status='completed'
        ).exclude(quality_rating=None).aggregate(average_rating=Avg('quality_rating'))['average_rating']
        return average
    
    def av_response_time(instance):
        average = PurchaseOrder.objects.filter(
        vendor=instance.vendor,
        acknowledgment_date__isnull=False
        ).aggregate(average=Avg(F('acknowledgment_date') - F('issue_date')))['average']
        return average
    
    def update_fulfillment_rate(instance):
        fulfilled_count = PurchaseOrder.objects.filter(
            vendor=instance.vendor,
            status='completed',
            issues__isnull=True
        ).count()
        total_po_count = PurchaseOrder.objects.filter(
            vendor=instance.vendor
        ).count()
        rate = 0
        if total_po_count > 0:
            rate = fulfilled_count / total_po_count
        return rate
    
    
    

    
    
