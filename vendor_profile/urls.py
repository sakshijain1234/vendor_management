from django.urls import path
from . import views

urlpatterns = [
    path('',views.profile),
    path('<str:vendor_code>/',views.modify_profile),
    path('<str:vendor_code>/performance',views.performance)
    ]