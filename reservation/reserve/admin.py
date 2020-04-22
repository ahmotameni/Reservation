from django.contrib import admin

from .models import *

admin.site.register(Food)
admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Order)
admin.site.register(TableStatusPerHour)
admin.site.register(Opinion)
admin.site.register(VIPCustomers)
admin.site.register(CustomersFavorites)

