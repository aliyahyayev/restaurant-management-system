from decimal import Decimal
from rest_framework import serializers
from .models import MenuItem, Table, Reservation, Order, OrderItem, Inventory

# 1. Menu Item Serializer
class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = '__all__'


# 2. Table Serializer
class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'


# 3. Inventory Serializer
class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


# 4. Reservation Serializer
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'

    def create(self, validated_data):
        table = validated_data['table']
        table.status = 'reserved'
        table.save()
        return super().create(validated_data)


# 5. Order Item Serializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']
        read_only_fields = ['price']


# 6. Order Serializer (Düzəldilmiş Versiya)
# 6. Order Serializer
class OrderSerializer(serializers.ModelSerializer):
    # 'required=False' əlavə edirik ki, status dəyişəndə yeməkləri yenidən istəməsin!
    items = OrderItemSerializer(many=True, required=False) 

    class Meta:
        model = Order
        fields = ['id', 'table', 'status', 'total_amount', 'items', 'created_at']

    class Meta:
        model = Order
        fields = ['id', 'table', 'status', 'total_amount', 'items', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        
        total = 0
        for item_data in items_data:
            menu_item = item_data['menu_item']
            quantity = item_data['quantity']
            price = menu_item.price
            
            # --- ANBARIN AVTOMATİK YENİLƏNMƏSİ ---
            if menu_item.category == 'main_course':
                cheese = Inventory.objects.filter(ingredient_name__iexact='Cheese').first()
                if cheese:
                    required_cheese = Decimal('0.2') * quantity
                    if cheese.quantity < required_cheese:
                        raise serializers.ValidationError(f"Not enough Cheese in inventory! Available: {cheese.quantity}kg")
                    cheese.quantity -= required_cheese
                    cheese.save()

                tomato = Inventory.objects.filter(ingredient_name__iexact='Tomato').first()
                if tomato:
                    required_tomato = Decimal('0.15') * quantity
                    if tomato.quantity < required_tomato:
                        raise serializers.ValidationError(f"Not enough Tomato in inventory! Available: {tomato.quantity}kg")
                    tomato.quantity -= required_tomato
                    tomato.save()
            # -------------------------------------
    
            OrderItem.objects.create(order=order, menu_item=menu_item, quantity=quantity, price=price)
            total += price * quantity

        order.total_amount = total
        
        if order.table:
            order.table.status = 'occupied'
            order.table.save()
            
        order.save()
        return order
    def update(self, instance, validated_data):
        # Köhnə statusu yaddaşda saxlayırıq
        old_status = instance.status
        
        # Standart yeniləməni icra edirik
        instance = super().update(instance, validated_data)
        
        # Əgər status dəyişibsə və paid/cancelled olubsa masanı azad edirik
        if old_status != instance.status and instance.status in ['paid', 'cancelled']:
            if instance.table:
                instance.table.status = 'available'
                instance.table.save()
                
        return instance