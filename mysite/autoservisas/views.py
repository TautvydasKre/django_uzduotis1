from django.shortcuts import render
from .models import Order, Service, Car

def index(request):
    # Gauti statistikos duomenis
    services_count = Service.objects.count()
    orders_count = Order.objects.count()
    cars_count = Car.objects.count()

    context = {
        'num_services': services_count,
        'num_orders': orders_count,
        'num_cars': cars_count,
    }
    return render(request, 'index.html', context)
