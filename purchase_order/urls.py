from django.urls import path
from . import views

urlpatterns = [
    path('',views.order),
    path('<str:po_number>/',views.modify_order),
    path('<str:po_number>/acknowledge/',views.acknowledgement)
]