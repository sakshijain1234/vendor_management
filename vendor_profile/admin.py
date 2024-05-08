from django.contrib import admin
from vendor_profile.models import vendor_model,PerformanceRecord

admin.site.register(vendor_model)
admin.site.register(PerformanceRecord)

# Register your models here.
