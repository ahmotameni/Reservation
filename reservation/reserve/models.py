from django.db import models
photo_path = 'img/'


class Customer(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()

    def __str__(self):
        return self.username


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    logo = models.ImageField()
    score = models.FloatField()  # should be calculated from data in Opinion class

    def __str__(self):
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=photo_path)
    price = models.SmallIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Table(models.Model):
    num_of_sits = models.SmallIntegerField()
    price = models.SmallIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    details = models.CharField(max_length=200)
    status = models.BooleanField(default=True)


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    num_of_customers = models.SmallIntegerField()
    text = models.CharField(max_length=200, default='')


class TableStatusPerHour(models.Model):
    time = models.DateTimeField()
    status = models.BooleanField()  # True: available / False: in use
    table = models.ForeignKey(Table, on_delete=models.CASCADE)


class Opinion(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    score = models.SmallIntegerField(default=0)


class VIPCustomers(models.Model):  # VIP Customers for each restaurant
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)


class CustomersFavorites(models.Model):  # Favorite orders of each customer
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
