from django.db import models

# Create your models here.

class Car(models.Model):
    """This model defines a car that is brought for a service."""
    national_number = models.CharField(verbose_name="Car national number", max_length=10)
    car_model = models.ForeignKey('CarModel', on_delete = models.CASCADE)
    vin_code = models.CharField(verbose_name="Vin code of the car", max_length=50)
    client = models.CharField(verbose_name="Client Name", max_length=50)

    def __str__(self):
        return f"{self.national_number} - {self.client}"

class Order(models.Model):
    """This model defines an order that was made for the car."""
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    total_price = models.DecimalField(verbose_name="Total Price", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order for  {self.car} on {self.date} - Total: {self.total_price}"

class CarModel(models.Model):
    """This model defines car model."""
    brand = models.CharField(verbose_name="Brand name", max_length=100)
    car_model = models.CharField(verbose_name="Car model", max_length=100)

    def __str__(self):
        return f"{self.brand} {self.car_model}"

class OrderLine(models.Model):
    """This model defines the line items in an order."""
    service = models.ForeignKey('Service', on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name="Quantiti of the order")
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} x {self.service.title} - {self.price}"

class Service(models.Model):
    """This model defines the services available."""
    title = models.CharField(verbose_name="Title of the service", max_length=50)
    price = models.DecimalField(verbose_name="Price of the service", max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.title} - Price: {self.price}"