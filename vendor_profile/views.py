from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import vendors_serializer
from .serializers import vendor_serializer
from .serializers import performance_serializer
from .models import vendor_model,PerformanceRecord

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
    
@api_view(["GET"])
def performance(request,vendor_code):
    try:
        query_set=PerformanceRecord.objects.get(vendor=vendor_code)
    except PerformanceRecord.DoesNotExist:
        return Response({"message": "Vendor not found"})
    serializer=performance_serializer(instance=query_set)
    data = {
        "vendor":vendor_code,
        "date": serializer.date(),
        "on_time_delivery_rate": serializer.delivery_rate(query_set),
        "quality_rating_avg": serializer.av_quality_rating(query_set),
        "average_response_time": serializer.av_response_time(query_set),
        "fulfillment_rate": serializer.update_fulfillment_rate(query_set)
    }
    if serializer.is_valid():
        return Response({"message":"performance of ","data":serializer.data})
    return Response(serializer.errors)