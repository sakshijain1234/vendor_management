from datetime import timezone,datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import PurchaseOrder
from .serializers import po_serializer

# Create your views here.
@api_view(["GET","POST"])
def order(request):
    if request.method=="GET":
        query_set=PurchaseOrder.objects.all()
        serializer=po_serializer(query_set,many=True)
        return Response(serializer.data)
    elif request.method=="POST":
        data=request.data
        serializer=po_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "Purchase order created successfully",
            "data": serializer.data
        })
        return Response(serializer.errors)

@api_view(["GET","PUT","DELETE"])
def modify_order(request,po_number):
    if request.method=="GET":
        try:
            query_set=PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            return Response({"message": "Order does not Exist"})
        serializer=po_serializer(query_set)
        return Response({"message":"GET","data":serializer.data})
    elif request.method=="PUT":
        try:
            query_set=PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            return Response({"message": "Order does not Exist"})
        data=request.data
        serializer=po_serializer(instance=query_set,data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            "message": "Order Updated successfully",
            "data": serializer.data
        })
        return Response(serializer.errors)
    elif request.method=="DELETE":
        try:
            query_set=PurchaseOrder.objects.get(po_number=po_number)
        except PurchaseOrder.DoesNotExist:
            return Response({"message": "Order does not Exist"})
        query_set.delete()
        query_sets=PurchaseOrder.objects.all()
        serializer=po_serializer(query_sets,many=True)
        return Response({"message":"Order deleted successfully","data":serializer.data})

@api_view(["POST"])
def acknowledgement(request,po_number):
    try:
        purchase_order = PurchaseOrder.objects.get(po_number=po_number)
    except PurchaseOrder.DoesNotExist:
        return Response({'error': 'Purchase order not found'})
    if purchase_order.acknowledgment_date is not None:
        return Response({'error': 'Purchase order already acknowledged'})
    purchase_order.acknowledgment_date = datetime.now(timezone.utc)
    purchase_order.save()
    return Response({"message":"Order acknowledged completed"})