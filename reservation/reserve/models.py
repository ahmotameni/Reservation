from django.db import models


class Customer(models.Model):
    username = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.PositiveIntegerField()
    # ToDo: add some other things like "Favorites" or "Past Orders"


class Restaurant(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=500)
    logo = models.ImageField()
    score = models.FloatField()
    # ToDo: add tables and...


class Order(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    num_of_customers = models.SmallIntegerField()
    customers_opinion = models.CharField(max_length=200)
    customers_score = models.SmallIntegerField()


class Food(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField()
    price = models.SmallIntegerField()
    # Todo: add opinions


class Table(models.Model):
    num_of_sits = models.SmallIntegerField()
    price = models.SmallIntegerField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    # ToDo: add status for each hour


