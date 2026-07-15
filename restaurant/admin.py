from django.contrib import admin
from .models import MenuItem, Table, Reservation, Order, OrderItem, Inventory

# Modellərimizi admin panelə əlavə edirik
admin.site.register(MenuItem)
admin.site.register(Table)
admin.site.register(Reservation)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Inventory)