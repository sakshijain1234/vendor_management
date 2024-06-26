# from rest_framework import serializers
# from .models import vendor_model,PerformanceRecord
# from purchase_order.models import PurchaseOrder
# from django.db.models import F,Avg
# from django.utils import timezone
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
# class performance_serializer(serializers.ModelSerializer):
#     date = serializers.SerializerMethodField()
#     Delivery_rate = serializers.SerializerMethodField()
#     av_quality_rating = serializers.SerializerMethodField()
#     av_response_time = serializers.SerializerMethodField()
#     update_fulfillment_rate = serializers.SerializerMethodField()

#     class Meta:
#         model=PerformanceRecord
#         fields="__all__"

#     def date(self,obj):
#         today=datetime.now(timezone.utc)
#         return today

#     def Delivery_rate(self,obj):
#         vendor_code=self.context.get('vendor_code')
#         on_time_count = PurchaseOrder.objects.filter(
#         vendor=vendor_code,
#         status='completed',
#         delivery_date__lte=F("issue_date")
#         ).count()
#         total_completed_count = PurchaseOrder.objects.filter(
#         vendor=vendor_code,
#         status='completed'
#         ).count()
#         rate = 0
#         if total_completed_count > 0:
#             rate = on_time_count/total_completed_count
#         return rate
    
#     def av_quality_rating(self,obj):
#         vendor_code=self.context.get('vendor_code')
#         average = PurchaseOrder.objects.filter(
#         vendor=vendor_code,
#         status='completed'
#         ).exclude(quality_rating=None).aggregate(average_rating=Avg('quality_rating'))['average_rating']
#         return average
    
#     def av_response_time(self,obj):
#         vendor_code=self.context.get('vendor_code')
#         average = PurchaseOrder.objects.filter(
#         vendor=vendor_code,
#         acknowledgment_date__isnull=False
#         ).aggregate(average=Avg(F('acknowledgment_date') - F('issue_date')))['average']
#         return average
    
#     def update_fulfillment_rate(self,obj):
#         vendor_code=self.context.get('vendor_code')
#         fulfilled_count = PurchaseOrder.objects.filter(
#             vendor=vendor_code,
#             status='completed',
#             issue_date__isnull=True
#         ).count()
#         total_po_count = PurchaseOrder.objects.filter(
#             vendor=vendor_code
#         ).count()
#         rate = 0
#         if total_po_count > 0:
#             rate = fulfilled_count / total_po_count
#         return rate
    
    
    

    
    
