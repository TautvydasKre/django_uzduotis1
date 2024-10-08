from django.contrib import admin
from .models import Car, Order, CarModel, OrderLine, Service
# Register your models here.

admin.site.register(Car)
admin.site.register(Order)
admin.site.register(CarModel)
admin.site.register(OrderLine)
admin.site.register(Service)