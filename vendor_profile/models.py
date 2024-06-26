from django.db import models
from django.utils import timezone

# Create your models here.
class vendor_model(models.Model):
    name=models.CharField(max_length=100)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(max_length=20,unique=True,primary_key=True)
    on_time_delivery_rate=models.DecimalField(max_digits=5, decimal_places=2)
    quality_rating_avg=models.DecimalField(max_digits=5, decimal_places=2)
    average_response_time=models.DecimalField(max_digits=5, decimal_places=2)
    fulfillment_rate=models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.name

class PerformanceRecord(models.Model):
    vendor = models.ForeignKey(vendor_model, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()