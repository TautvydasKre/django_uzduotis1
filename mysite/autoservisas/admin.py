from django.contrib import admin
from .models import Car, Order, CarModel, OrderLine, Service
# Register your models here.

class OrderLineInline(admin.TabularInline):  # Changed name to OrderLineInline
    model = OrderLine
    extra = 1
    fields = ['service', 'quantity', 'price']
    readonly_fields = ['total_price']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['get_car_model', 'car', 'date','get_service_titles','total_amount']
    list_filter = ['date']
    inlines = [OrderLineInline]

    def get_service_titles(self, obj):
        return ', '.join([line.service.title for line in obj.orderline_set.all() if line.service])

    get_service_titles.short_description = 'Services'

    def get_car_model(self, obj):
        return obj.car.car_model

    get_car_model.short_description = 'car_model'

    def total_ammount(self, obj):
        return obj.total_amount()

    total_ammount.short_description = 'Total Amount'

class OrderLineAdmin(admin.ModelAdmin):
    list_display = ['service', 'order', 'quantity', 'price']
    readonly_fields = ['total_price']


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    list_filter = ['title']

class CarAdmin(admin.ModelAdmin):
    list_display = ['car_model', 'client_name', 'vin_code', 'car_plate']
    search_fields = ['client_name', 'car_model', 'car_plate','vin_code']
    list_filter = ['car_model','client_name']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['brand', 'car_model']
    search_fields = ['brand', 'car_model']

admin.site.register(Car, CarAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CarModel, CarModelAdmin)
admin.site.register(OrderLine, OrderLineAdmin)  # Consider if you want this to be separately editable
admin.site.register(Service, ServiceAdmin)
