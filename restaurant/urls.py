from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TableViewSet, MenuItemViewSet, OrderViewSet, ReservationViewSet

router = DefaultRouter()
router.register(r'tables', TableViewSet, basename='table')
router.register(r'menu', MenuItemViewSet, basename='menu')
router.register(r'orders', OrderViewSet, basename='order')
# Bura mütləq diqqət et! 'reservations' router-ə qeydiyyatdan keçməlidir:
router.register(r'reservations', ReservationViewSet, basename='reservation')

urlpatterns = [
    path('', include(router.urls)),
]