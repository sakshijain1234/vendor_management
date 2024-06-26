from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import vendors_serializer
from .serializers import vendor_serializer

from .models import vendor_model

from rest_framework.views import APIView
from .serializers import performance_serializer
from purchase_order.models import PurchaseOrder
from django.db.models import Avg, Count, F, Q
from rest_framework import status
from datetime import timedelta

# Create your views here.

@api_view(["GET","POST"])
def profile(request):
    if request.method=="GET":
        query_set=vendor_model.objects.all()
        serializer=vendors_serializer(query_set,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        data=request.data
        serializer=vendors_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "Vendor created successfully",
            "data": serializer.data
        })
        return Response(serializer.errors)

@api_view(["GET","PUT","DELETE"])
def modify_profile(request,vendor_code):
    if request.method=="GET":
        try:
            query_set=vendor_model.objects.get(vendor_code=vendor_code)
        except vendor_model.DoesNotExist:
            return Response({"message": "Vendor not found"})
        serializer=vendor_serializer(query_set)
        return Response({"message":"GET","data":serializer.data})
    elif request.method=="PUT":
        try:
            query_set=vendor_model.objects.get(vendor_code=vendor_code)
        except vendor_model.DoesNotExist:
            return Response({"message": "Vendor not found"})
        data=request.data
        serializer=vendor_serializer(instance=query_set,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "Vendor Updated successfully",
            "data": serializer.data
        })
        return Response(serializer.errors)
    elif request.method=="DELETE":
        try:
            query_set=vendor_model.objects.get(vendor_code=vendor_code)
        except vendor_model.DoesNotExist:
            return Response({"message": "Vendor not found"})
        query_set.delete()
        query_sets=vendor_model.objects.all()
        serializer=vendors_serializer(query_sets,many=True)
        return Response({"message":"Vendor deleted successfully","data":serializer.data})
    
# @api_view(["GET"])
# def performance(request,vendor_code):
#     serializer=performance_serializer(context={'vendor_code':vendor_code})
#     return Response(serializer.data)

class VendorPerformanceView(APIView):
    def get(self, request, vendor_code):
        try:
            vendor = vendor_model.objects.get(vendor_code=vendor_code)
        except vendor_model.DoesNotExist:
            # Use the Vendor class directly in the exception handling
            return Response({"error": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)

        # Only proceed if the vendor is found
        self.update_vendor_performance(vendor)
        serializer = performance_serializer(vendor)
        return Response(serializer.data)

    def update_vendor_performance(self, vendor):
        # Get all completed orders for the vendor
        completed_orders = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_completed_orders = completed_orders.count()

        # Calculate on-time delivery rate
        if total_completed_orders > 0:
            on_time_deliveries = completed_orders.filter(delivery_date__lte=F('delivery_date')).count()
            vendor.on_time_delivery_rate = (on_time_deliveries / total_completed_orders) * 100
        else:
            vendor.on_time_delivery_rate = 0.0

        # Calculate quality rating average
        quality_ratings = completed_orders.filter(quality_rating__isnull=False).aggregate(avg_rating=Avg('quality_rating'))
        vendor.quality_rating_avg = quality_ratings['avg_rating'] if quality_ratings['avg_rating'] else 0.0

        # Calculate average response time
        response_times = completed_orders.filter(acknowledgment_date__isnull=False).annotate(
            response_time=F('acknowledgment_date') - F('issue_date')
        ).aggregate(avg_response_time=Avg('response_time'))

        # Convert response time to hours
        vendor.average_response_time = response_times['avg_response_time'].total_seconds() / 3600 if response_times['avg_response_time'] else 0.0

        # Calculate fulfillment rate
        total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
        vendor.fulfillment_rate = (total_completed_orders / total_orders) * 100 if total_orders > 0 else 0.0

        vendor.save()