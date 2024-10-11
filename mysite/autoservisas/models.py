from django.db import models

# Create your models here.

class Car(models.Model):
    """This model defines a car that is brought for a service."""
    car_plate = models.CharField(verbose_name="Car national number", max_length=10)
    car_model = models.ForeignKey('CarModel', on_delete = models.CASCADE)
    vin_code = models.CharField(verbose_name="Vin code of the car", max_length=50)
    client_name = models.CharField(verbose_name="Client Name", max_length=50)

    def __str__(self):
        return f"{self.car_plate} - {self.client_name}"

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'


from django.db import models


class Order(models.Model):
    """This model defines an order that was made for the car."""

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    date = models.DateField(verbose_name="Data", auto_now_add=True)
    car = models.ForeignKey('Car', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='Order Status'
    )

    def total_amount(self):
        """Calculate the total sum of all order Lines."""
        order_lines = self.orderline_set.all()
        return sum(line.total_price() for line in order_lines)

    def __str__(self):
        return f"Order for {self.car} on {self.date} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class CarModel(models.Model):
    """This model defines car model."""
    brand = models.CharField(verbose_name="Brand name", max_length=100)
    car_model = models.CharField(verbose_name="Car model", max_length=100)

    def __str__(self):
        return f"{self.brand} {self.car_model}"

    class Meta:
        verbose_name = "Car Model"
        verbose_name_plural = "Car Models"

class OrderLine(models.Model):
    """This model defines the line items in an order."""
    service = models.ForeignKey('Service', on_delete=models.SET_NULL, null=True,blank=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantity of the order")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)

    def total_price(self):
        """Calculate the total price by multiplying the service price with quantiti"""
        if self.service and self.quantity:
            return self.service.price * self.quantity
        return 0

    total_price.short_description = 'Summ'

    def __str__(self):
        return f"{self.quantity} x {self.service.title} - {self.price}"

    class Meta:
        verbose_name = 'Order Line'
        verbose_name_plural = 'Order Lines'

class Service(models.Model):
    """This model defines the services available."""
    title = models.CharField(verbose_name="Title of the service", max_length=50)
    price = models.DecimalField(verbose_name="Price of the service", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'