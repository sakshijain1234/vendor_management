from django.urls import path
from . import views
from .views import VendorPerformanceView

urlpatterns = [
    path('',views.profile),
    path('<str:vendor_code>/',views.modify_profile),
    path('<str:vendor_code>/performance/', VendorPerformanceView.as_view(), name='vendor-performance'),
    ]