from django.db import models
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.authentication import BasicAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny# Giriş şərti
from .permissions import IsManager # İndi yazdığımız menecer şərti
from .models import MenuItem, Table, Inventory, Reservation, Order
from .serializers import (
    MenuItemSerializer, TableSerializer, InventorySerializer, 
    ReservationSerializer, OrderSerializer
)

# 1. Menu Item API (Hər kəs baxa bilər, amma giriş edənlər baxa bilsin)
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


# 2. Table API 
class TableViewSet(viewsets.ModelViewSet):
    serializer_class = TableSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Table.objects.all()
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


# 3. Inventory API (YALNIZ MENECER üçün!)
class InventoryViewSet(viewsets.ModelViewSet):
    serializer_class = InventorySerializer
    # Bura 'IsManager' qoyuruq. Artıq adi işçilər bura daxil ola bilməyəcək:
    permission_classes = [IsManager] 

    def get_queryset(self):
        queryset = Inventory.objects.all()
        low_stock = self.request.query_params.get('low_stock')
        if low_stock == 'true':
            queryset = queryset.filter(quantity__lte=models.F('low_stock_threshold'))
        return queryset

# CSRF yoxlamasını API sorğuları üçün dövrədən çıxaran köməkçi sinif:
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # Heç bir CSRF yoxlaması etmə, keçsin

# 4. Reservation API
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    
    # SessionAuthentication-u tamamilə kənara qoyuruq! 
    # Yalnız JWT və Basic qoşuruq ki, brauzer sessiyası (cookie) CSRF xətası yaratmasın.
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    
    # Hamıya icazə veririk
    permission_classes = [AllowAny]
    
    # get_permissions metodunu tamamilə silirik və ya düzgün obyekt qaytarırıq:
    def get_permissions(self):
        return [AllowAny()]


# 5. Order API (Sifarişi hər kəs vura bilər)
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    # Bu iki sətir brauzerdən gələn 403 CSRF blokunu tamamilə qırır:
    # Sistemi yalnız JWT və Basic authentication ilə işləməyə məcbur edirik.
    authentication_classes = [JWTAuthentication, BasicAuthentication]
    

# UI Səhifəsini render edən sadə view
def home_ui(request):
    return render(request, 'index.html')