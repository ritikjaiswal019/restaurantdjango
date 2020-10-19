from django.urls import path
from . import views

urlpatterns = [
    path("", views.index ,name="index"),
    path("admin/",views.admin, name= "admin"),
    path("worker/", views.worker, name = "worker"),
    path("customer/",views.customer, name= "customer")
]